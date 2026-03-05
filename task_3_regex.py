import re

def normalize_phone(phone_number: str) -> str:
    # Remove all characters except digits and '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    if cleaned.startswith("380"):
        return f"+{cleaned}"
    
    if cleaned.startswith("0"):
        return f"+38{cleaned}"

    if cleaned.startswith("+"):
        return cleaned

    return f"+{cleaned}"
    