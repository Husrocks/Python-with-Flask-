# Global savings box (shared by everyone)
saving_box = 100  # Initial money

def add_money(amount):
    """Put money into the saving box."""
    global saving_box  # Tell Python we are using the global saving box
    saving_box += amount
    print(f"You added ${amount}. Total in saving box: ${saving_box}")

def take_money(amount):
    """Take money out of the saving box."""
    global saving_box  # Using the same saving box
    if saving_box >= amount:
        saving_box -= amount
        print(f"You took ${amount}. Remaining: ${saving_box}")
    else:
        print(f"Not enough money! You only have ${saving_box}")

# Checking the saving box
print(f"Starting Saving Box: ${saving_box}")

# Doing some transactions
add_money(50)    # Adding $50
take_money(30)   # Taking $30
take_money(200)  # Trying to take more than available
add_money(800)  # Trying to take even more

# Final Saving Box Value
print(f"Final Saving Box: ${saving_box}")
