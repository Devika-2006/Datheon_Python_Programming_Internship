import re

BUSINESS_HOURS = "Our business hours are Monday to Friday, 9:00 AM to 6:00 PM IST. We are closed on weekends."
FAQS = {
    "shipping": "Standard shipping usually takes 3–5 business days. Delivery times may vary by location.",
    "returns": "You can request a return within 30 days of delivery, provided the item is unused and in its original packaging.",
    "payment": "We accept major credit and debit cards, UPI, and net banking.",
    "support": "You can reach our support team by emailing support@example.com during business hours.",
}
EXIT_COMMANDS = {"bye", "exit", "quit"}


def normalize(text):
    """Lowercase input and collapse extra whitespace."""
    return re.sub(r"\s+", " ", text.strip().lower())


def matches(pattern, text):
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


def get_responses(user_text):
    """Return all applicable responses so one message can match multiple intents."""
    text = normalize(user_text)
    responses = []

    if matches(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", text):
        responses.append("Hello! I can help with business hours, shipping, returns, payment, or support contact details.")

    if matches(r"\b(hours?|open|close|closing|opening|when.*(available|work))\b", text):
        responses.append(BUSINESS_HOURS)

    faq_patterns = {
        "shipping": r"\b(ship|shipping|delivery|deliver|dispatch|tracking)\b",
        "returns": r"\b(return|refund|exchange|replace|replacement)\b",
        "payment": r"\b(pay|payment|payments|card|upi|net banking|checkout)\b",
        "support": r"\b(contact|support|help|email|reach|customer service)\b",
    }
    for topic, pattern in faq_patterns.items():
        if matches(pattern, text):
            responses.append(FAQS[topic])

    if not responses:
        responses.append("Sorry, I didn't understand that. Ask me about business hours, shipping, returns, payment, or support.")

    return responses


def main():
    print("Support Assistant: Hello! Ask me a question, or type 'bye', 'exit', or 'quit' to leave.")

    while True:
        try:
            user_text = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nSupport Assistant: Goodbye!")
            break

        text = normalize(user_text)
        if not text:
            print("Support Assistant: Please type a question, or type 'bye' to leave.")
            continue
        if text in EXIT_COMMANDS:
            print("Support Assistant: Goodbye! Thanks for contacting us.")
            break

        for response in get_responses(user_text):
            print(f"Support Assistant: {response}")


if __name__ == "__main__":
    main()
