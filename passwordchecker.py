import re
import os

def load_common_passwords(filepath='common_passwords.txt'):
    """Loads a list of common passwords from a file."""
    if not os.path.exists(filepath):
        print(f"Warning: '{filepath}' not found. Dictionary check will be skipped.")
        return set()
    with open(filepath, 'r') as f:
        return set(line.strip().lower() for line in f)

def check_password_strength(password, common_passwords):
    """
    Analyzes the strength of a password based on several criteria.

    Returns a tuple: (score, feedback_messages)
    """
    score = 0
    feedback = []

    # 1. Length Check
    min_length = 8
    if len(password) >= min_length:
        score += 2
        feedback.append(f"Length: Good ({len(password)} characters)")
    elif len(password) >= 6:
        score += 1
        feedback.append(f"Length: Okay ({len(password)} characters). Consider making it longer (min {min_length}).")
    else:
        feedback.append(f"Length: Too short ({len(password)} characters). Must be at least {min_length}.")

    # 2. Character Variety Check
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_symbol = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    char_types = 0
    if has_lowercase:
        char_types += 1
    if has_uppercase:
        char_types += 1
    if has_digit:
        char_types += 1
    if has_symbol:
        char_types += 1

    if char_types >= 4:
        score += 3
        feedback.append("Variety: Excellent (includes lowercase, uppercase, numbers, and symbols).")
    elif char_types >= 3:
        score += 2
        feedback.append("Variety: Good (includes at least 3 types of characters).")
    elif char_types >= 2:
        score += 1
        feedback.append("Variety: Moderate (includes at least 2 types of characters). Add more variety for better strength.")
    else:
        feedback.append("Variety: Low (needs more diverse characters).")

    if not has_lowercase:
        feedback.append("- Add lowercase letters.")
    if not has_uppercase:
        feedback.append("- Add uppercase letters.")
    if not has_digit:
        feedback.append("- Add numbers.")
    if not has_symbol:
        feedback.append("- Add symbols (e.g., !@#$%^&*).")

    # 3. Dictionary Word Check
    if password.lower() in common_passwords:
        score -= 5 # Penalize heavily for dictionary words
        feedback.append("Dictionary Check: WARNING! Your password is a common dictionary word. This is very weak!")
    else:
        feedback.append("Dictionary Check: Not found in common password list.")

    # 4. Sequential/Repeated Character Check (Bonus)
    if re.search(r'(.)\1\1', password): # Checks for 3 or more repeating characters (e.g., 'aaa', '111')
        score -= 2
        feedback.append("Pattern: Avoid repeating characters (e.g., 'aaa', '111').")
    if re.search(r'abc|123|qwe', password.lower()): # Simple check for common sequences
        score -= 2
        feedback.append("Pattern: Avoid common sequences (e.g., 'abc', '123', 'qwerty').")

    return score, feedback

def main():
    print("--- Password Strength Checker ---")
    print("Enter a password to check its strength (or type 'exit' to quit).")

    common_passwords = load_common_passwords()

    while True:
        password = input("\nEnter your password: ")
        if password.lower() == 'exit':
            break

        score, feedback_messages = check_password_strength(password, common_passwords)

        print("\n--- Password Analysis ---")
        for msg in feedback_messages:
            print(msg)

        print(f"\nOverall Score: {score}")

        if score >= 5:
            print("Verdict: Strong Password!")
        elif score >= 2:
            print("Verdict: Moderate Password. Consider improving it.")
        else:
            print("Verdict: Weak Password. Change it immediately!")

if __name__ == "__main__":
    main()