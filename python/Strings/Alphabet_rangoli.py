import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3
    lines = []
    
    # Generate the top half and middle line
    for i in range(size):
        # Slices the required characters from the alphabet and reverses them
        left_side = [alphabet[j] for j in range(size - 1, size - 1 - i - 1, -1)]
        # Mirrors the letters to create the full sequence for the row
        full_row = left_side + left_side[:-1][::-1]
        # Joins with hyphens and pads the sides
        lines.append("-".join(full_row).center(width, "-"))
        
    # Append the bottom half (the top half reversed, skipping the middle line)
    full_rangoli = lines + lines[:-1][::-1]
    
    # Print the entire structure joined by newlines
    print("\n".join(full_rangoli))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)