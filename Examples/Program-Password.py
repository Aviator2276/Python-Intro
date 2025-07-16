#START
#INPUT - FROM USER
# Here we are getting input from the user and assigning them to their
# respective variables
website = input(str("What website will you be using this password for? "))
abbr = input(str("What is a two-letter abbreviation for this website? "))
verb = input(str("What is a verb that describes how you use this website? "))
content = input(str("What content is on this website? "))

#OPERATIONS
# These ensure that even if the user typed an uppercase or lowercase, it will
# either one depending on the user of the variable.
website = website.lower()
abbr = abbr.upper()
content = content.upper()
verb.lower()
#VARIABLES
# Here we are setting up are variables to be ready for use in the FOR loop or
# to be printed
length = len(website)
# Here we defined our vowels to cycle through and compare against
vowels = ["a","e","i","o","u"]
# We stash the new variable as changeVerb which will be verb but with no
# vowels
changeVerb = verb
# Count ensures we stay on track for the amount of letters available in verb
count = 0

#LOOP
# This loop loops through the verb and compares each letter with each vowel
# in the vowel variable
for i in verb:
    for v in vowels:
        if v == verb[count]:
            # If the letter matches with vowel, remove it
            changeVerb = changeVerb.replace(verb[count], "")
    # This keeps track what letter we're on
    count = count + 1
    
#OUTPUT
# Finally we mash everything into a password
print("Here's your password!\n" + abbr + str(length) + changeVerb + content)
#END