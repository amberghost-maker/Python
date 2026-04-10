class RomanNumeralConverter:
    def int_to_roman(self, num: int) -> str:
        """
        Convert an integer to its Roman numeral equivalent.
        The number should be between 1 and 3999.
        """
        if not 1 <= num <= 3999:
            raise ValueError("Number must be between 1 and 3999")

        # Roman numeral mapping (in descending order)
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
            (1, "I")
        ]

        result = ""
        for value, symbol in roman_map:
            while num >= value:
                result += symbol
                num -= value

        return result


# Example usage
if __name__ == "__main__":
    converter = RomanNumeralConverter()
    
    try:
        number = int(input("Enter an integer (1-3999): "))
        roman = converter.int_to_roman(number)
        print(f"Roman numeral for {number} is: {roman}")
    except ValueError as e:
        print(f"Error: {e}")