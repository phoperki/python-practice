

def is_valid_email(email):
    # Checks variable
    checks = 0
    # Split on @ sign
    email_list=email.split("@")
    
    before = ""
    after = ""

    # Assign before and after @ variables
    if len(email_list) > 1:
        before = email_list[0]
        after = email_list[1]

    # Valid email must have:
    # - Exactly one @ symbol
    if email.count("@") == 1:
        checks = checks+1
    # - At least one character before the @
    # How to count characters in a string
    if len(before) >= 1:
        checks = checks+1
    # - At least one . after the @
    if after.count(".") >= 1:
        checks = checks+1
    # - At least one character after the final .
    after_period = after.split(".")

    if len(after_period[-1]) >=1:
        checks=checks+1
    # - No spaces anywhere
    if not email.count(" "):
        checks=checks+1
    # Return True if valid, False if not

    if checks == 5:
        return True
    else:
        return False
    pass

# Test cases
print(is_valid_email("user@example.com"))      # Should be True
print(is_valid_email("invalid.email.com"))     # Should be False (no @)
print(is_valid_email("@example.com"))          # Should be False (nothing before @)
print(is_valid_email("user@com"))              # Should be False (no . after @)
print(is_valid_email("user @example.com"))     # Should be False (has space)
print(is_valid_email("user@example."))         # Should be False (nothing after .)
print(is_valid_email("my.name@company.co.uk")) # Should be True