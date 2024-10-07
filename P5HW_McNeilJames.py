# James McNeil
# 10/2/24
# P5HW
# Making a game using python

def create_character():
    # Prompt the user for the superhero's attributes
    hero_name = input("Enter the superhero's name: ")
    super_strength = input("Enter the superhero's super strength (e.g., 'high', 'medium', 'low'): ")
    super_speed = input("Enter the superhero's super speed (e.g., 'high', 'medium', 'low'): ")
    super_intellect = input("Enter the superhero's super intellect (e.g., 'high', 'medium', 'low'): ")
    
    # Create and return the character dictionary
    character = {
        'hero_name': hero_name,
        'super_strength': super_strength,
        'super_speed': super_speed,
        'super_intellect': super_intellect
    }
    
    return character


def display_characters(char_list):
    for char in char_list:
        for key, value in char.items():
            print(f'{key}: {value}')
        print()

        

def attack_hero(attacker, victim):
    print()
    print(f"****{attacker['hero_name']} is attacking {victim['hero_name']}**** ")
    print()
    # Define how much to transfer (you can adjust these values)
    strength_transfer = 1  # Amount to transfer from victim's strength
    speed_transfer = 1      # Amount to transfer from victim's speed

    # Update the victim's attributes
    victim['super_strength'] = max('low', 
                                    'medium' if victim['super_strength'] == 'high' else 'low')
    victim['super_speed'] = max('low', 
                                 'medium' if victim['super_speed'] == 'high' else 'low')

    # Update the attacker's attributes
    if attacker['super_strength'] == 'low':
        attacker['super_strength'] = 'medium'
    elif attacker['super_strength'] == 'medium':
        attacker['super_strength'] = 'high'

    if attacker['super_speed'] == 'low':
        attacker['super_speed'] = 'medium'
    elif attacker['super_speed'] == 'medium':
        attacker['super_speed'] = 'high'


    return attacker, victim


# Example usage
if __name__ == "__main__":

    # Create a list
    char_list = []

    # Create two characters
    superhero_1 = create_character()
    superhero_2 = create_character()

    # Add characters to list
    char_list.append(superhero_1)
    char_list.append(superhero_2)


    # Display all characters
    display_characters(char_list)


    superhero_1, superhero_2 = attack_hero(superhero_1, superhero_2)

    # Display all characters
    display_characters(char_list)

