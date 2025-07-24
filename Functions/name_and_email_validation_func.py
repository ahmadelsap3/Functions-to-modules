def name_and_email_validation_func():
    name = input("Enter your name: ")
    while name.isalpha() == False or name.strip() == "":
        print("Invalid name. Please enter a valid name.")
        name = input("Enter your name: ")

    EMAIL_PROMPT = "Enter your email: "
    email = input(EMAIL_PROMPT)
    while "@" not in email or "." not in email:
        print("Invalid email. Please enter a valid email.")
        email = input(EMAIL_PROMPT)

    while email[0] in ["@", "."] or email[-1] in ["@", "."]:
        print("Invalid email. Email must not start with @ or .")
        email = input(EMAIL_PROMPT)

    while "@." in email or ".@" in email:
        print("Invalid email. Email must not contain @ followed by . or vice versa.")
        email = input(EMAIL_PROMPT)

    print("Name:", name)
    print("Email:", email)
    return name, email

if __name__ == "__main__":
    name_and_email_validation_func()
