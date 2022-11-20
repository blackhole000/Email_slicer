# collect email from user
# split the email using the @, the first part as the username, the secand part is ganno be saved as domain
# exaple: hello@codewith.com  hello codewith.com

def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Enter your email address: ")

    (username, domain) = email_input.split("@")   #hello -username
    (domain, extension) = domain.split(".")    # @codewithme - domain .com -extension

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
while True:
    main()




