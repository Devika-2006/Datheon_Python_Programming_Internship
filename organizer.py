"""Organize files in a folder into subfolders based on file extension.

Usage: python organizer.py PATH [--dry-run]
Only files directly inside PATH are organized; subfolders are left alone.
"""

import argparse
import logging
import shutil
from pathlib import Path


EXTENSION_CATEGORIES = {
    # Documents
    ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
    ".odt": "Documents", ".rtf": "Documents", ".txt": "Documents",
    ".xls": "Documents", ".xlsx": "Documents", ".csv": "Documents",
    ".ppt": "Documents", ".pptx": "Documents",
    # Images
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".gif": "Images", ".bmp": "Images", ".svg": "Images",
    ".webp": "Images", ".tif": "Images", ".tiff": "Images",
    # Videos
    ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos",
    ".mkv": "Videos", ".wmv": "Videos", ".webm": "Videos",
    # Audio
    ".mp3": "Audio", ".wav": "Audio", ".aac": "Audio",
    ".flac": "Audio", ".ogg": "Audio", ".m4a": "Audio",
    # Archives
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
    ".tar": "Archives", ".gz": "Archives",
    # Code
    ".py": "Code", ".js": "Code", ".ts": "Code", ".html": "Code",
    ".css": "Code", ".java": "Code", ".c": "Code", ".cpp": "Code",
    ".h": "Code", ".cs": "Code", ".go": "Code", ".rs": "Code",
    ".json": "Code", ".xml": "Code", ".yml": "Code", ".yaml": "Code",
    ".sh": "Code", ".bat": "Code", ".ps1": "Code",
}


def available_destination(destination: Path) -> Path:
    """Choose a destination that does not overwrite an existing file."""
    if not destination.exists():
        return destination

    stem, suffix = destination.stem, destination.suffix
    counter = 1
    while True:
        candidate = destination.with_name(f"{stem}_{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def organize(folder: Path, dry_run: bool = False) -> tuple[int, int]:
    moved = 0
    skipped = 0

    try:
        entries = list(folder.iterdir())
    except PermissionError as error:
        logging.error("Cannot read %s: %s", folder, error)
        return moved, 1

    for source in entries:
        # Leave directories and symbolic links untouched.
        if not source.is_file() or source.is_symlink():
            continue

        category = EXTENSION_CATEGORIES.get(source.suffix.lower())
        if category is None:
            logging.info("Skipped (unknown extension): %s", source.name)
            skipped += 1
            continue

        destination_folder = folder / category
        destination = available_destination(destination_folder / source.name)
        if dry_run:
            logging.info("Would move %s -> %s", source.name, destination.relative_to(folder))
            moved += 1
            continue

        try:
            destination_folder.mkdir(exist_ok=True)
            shutil.move(str(source), str(destination))
            logging.info("Moved %s -> %s", source.name, destination.relative_to(folder))
            moved += 1
        except (PermissionError, OSError) as error:
            logging.error("Could not move %s: %s", source.name, error)
            skipped += 1

    return moved, skipped


def main() -> None:
    parser = argparse.ArgumentParser(description="Sort files into extension-based subfolders.")
    parser.add_argument("folder", type=Path, help="Folder whose immediate files should be organized")
    parser.add_argument("--dry-run", action="store_true", help="Show planned moves without changing files")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    folder = args.folder.expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        parser.error(f"folder does not exist or is not a directory: {folder}")

    moved, skipped = organize(folder, dry_run=args.dry_run)
    verb = "would be relocated" if args.dry_run else "relocated"
    print(f"\nSummary: {moved} file(s) {verb}; {skipped} file(s) skipped or failed.")


if __name__ == "__main__":
    main()
