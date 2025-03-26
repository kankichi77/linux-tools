#!/usr/bin/env python3
import argparse
import random
import string

def randgen(length=12, allowed="1Aa"):
    # Validate length
    try:
        length = int(length)
        if not 1 <= length <= 256:
            raise ValueError
    except ValueError:
        raise ValueError("Length must be an integer between 1 and 256")

    # Define character sets
    digits = string.digits if "1" in allowed else ""
    uppercase = string.ascii_uppercase if "A" in allowed else ""
    lowercase = string.ascii_lowercase if "a" in allowed else ""
    symbols = ";-_=+()*&^%@!?><" if ";" in allowed else ""

    # Combine allowed characters
    char_pool = digits + uppercase + lowercase + symbols
    
    # Validate character pool
    if not char_pool:
        raise ValueError("No valid character types specified in allowed string")

    # Generate random string
    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Generate a random string with specified length and character types"
    )
    
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Length of string (1-256, default: 12)"
    )
    
    parser.add_argument(
        "-c", "--chars",
        type=str,
        default="1Aa",
        help="Allowed chars: '1'=numbers, 'A'=uppercase, 'a'=lowercase, ';'=symbols (default: '1Aa')"
    )

    # Parse arguments
    args = parser.parse_args()

    try:
        # Generate and print random string
        result = randgen(args.length, args.chars)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

