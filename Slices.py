
# Initial guest list
guests = ['Socrates', 'Seneca', 'Epictetus']

# Expanding the guest list
guests.append('Steve Jobs')
guests.append('Nikola Tesla')
guests.append('Leonardo da Vinci')

print("Good news! I found a bigger dinner table, so now there’s more space for guests!\n")

# Adding guests at different positions
guests.insert(0, 'Marcus Aurelius')
guests.insert(len(guests) // 2, 'Albert Einstein')
guests.append('Alan Turing')

# Sorting the guest list
guests.sort()

# Sending invitations
for guest in guests:
    print(f"Dear {guest}, Please join me for an unforgettable evening of food and drinks.")

# Print the first three items using slicing
print("\nThe first three items in the list are:")
print(guests[:3])

# Print three items from the middle using slicing
middle_index = len(guests) // 2
print("\nThree items from the middle of the list are:")
print(guests[middle_index - 1:middle_index + 2])

# Print the last three items using slicing
print("\nThe last three items in the list are:")
print(guests[-3:])
