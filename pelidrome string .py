text = "Nurses Run"

# Step 1: remove spaces and convert to lowercase
cleaned = text.replace(" ", "").lower()

# Step 2: compare with reverse
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")