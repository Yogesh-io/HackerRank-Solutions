def print_formatted(number):
    # Calculate the maximum width based on the binary representation of 'number'
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        # Format each number representation
        dec = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        # Print each value right-aligned to match the calculated width
        print(f"{dec.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)