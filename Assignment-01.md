
Person: 
- write a python code for the following question:
Implement a function to convert a given number to word either in Indian or Western form.

Example:

*  fig2words(81783456, "I") --> Eight crore seventeen lakh eighty three thousand four hundred and fifty six

* fig2words(81783456, "W") --> Eighty one million seven hundred and eighty three thousand four hundred and fifty six

* fig2words(181783456, "I") --> Eighteen crore seventeen lakh eighty three thousand four hundred and fifty six

* fig2words(26181783456, "W") --> Twenty six billion one hundred and eighty one million seven hundred and eighty three thousand four hundred and fifty six

ChatGPT: 
- You can implement the function `fig2words` using Python. Below is the code that achieves this:

```python
def fig2words(num, region):
    # Dictionary for Indian number system
    indian_numbers = {
        0: '',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
    }

    # Dictionary for Western number system
    western_numbers = {
        0: '',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
    }

    # Scale names
    scale_names = {
        2: 'Hundred',
        3: 'Thousand',
        5: 'Lakh',  # Indian
        7: 'Crore',  # Indian
        6: 'Million',  # Western
        9: 'Billion',  # Western
    }

    def convert_to_words(n, scale):
        if n == 0:
            return ''
        elif n < 20:
            return indian_numbers[n] if region == "I" else western_numbers[n]
        elif n < 100:
            return indian_numbers[(n // 10) * 10] + ' ' + convert_to_words(n % 10, scale)
        else:
            return indian_numbers[n // scale] + ' ' + scale_names[scale] + ' ' + convert_to_words(n % scale, scale)

    if region == "I":
        scale = 100
        final_scale = 10000000  # for Indian numbering system
    else:
        scale = 1000
        final_scale = 1000000  # for Western numbering system

    words = convert_to_words(num // final_scale, scale)
    remainder = convert_to_words(num % final_scale, scale)

    if remainder:
        if region == "I":
            words += ' Crore ' if num // final_scale > 1 else ' Crore'
        else:
            words += ' Million ' if num // final_scale > 1 else ' Million'

        words += remainder

    return words


# Test cases
print(fig2words(81783456, "I"))  # Eight crore seventeen lakh eighty three thousand four hundred and fifty six
print(fig2words(81783456, "W"))  # Eighty one million seven hundred and eighty three thousand four hundred and fifty six
print(fig2words(181783456, "I"))  # Eighteen crore seventeen lakh eighty three thousand four hundred and fifty six
print(fig2words(26181783456, "W"))  # Twenty six billion one hundred and eighty one million seven hundred and eighty three thousand four hundred and fifty six
```



This code first defines dictionaries for numbers up to 99 in both Indian and Western numbering systems, as well as scale names. Then, it defines a recursive function to convert a number to words based on the given region. Finally, it formats the output according to the input region and returns the result.

Person: 
- write only the function

ChatGPT: 
- Sure, here's the `fig2words` function without the test cases:

```python
def fig2words(num, region):
    indian_numbers = {
        0: '',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
    }

    western_numbers = {
        0: '',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
    }

    scale_names = {
        2: 'Hundred',
        3: 'Thousand',
        5: 'Lakh',  
        7: 'Crore',  
        6: 'Million',  
        9: 'Billion',  
    }

    def convert_to_words(n, scale):
        if n == 0:
            return ''
        elif n < 20:
            return indian_numbers[n] if region == "I" else western_numbers[n]
        elif n < 100:
            return indian_numbers[(n // 10) * 10] + ' ' + convert_to_words(n % 10, scale)
        else:
            return indian_numbers[n // scale] + ' ' + scale_names[scale] + ' ' + convert_to_words(n % scale, scale)

    if region == "I":
        scale = 100
        final_scale = 10000000  
    else:
        scale = 1000
        final_scale = 1000000  

    words = convert_to_words(num // final_scale, scale)
    remainder = convert_to_words(num % final_scale, scale)

    if remainder:
        if region == "I":
            words += ' Crore ' if num // final_scale > 1 else ' Crore'
        else:
            words += ' Million ' if num // final_scale > 1 else ' Million'

        words += remainder

    return words
```



This function takes a number `num` and a region (`"I"` for Indian, `"W"` for Western) as input and returns the corresponding number in words based on the specified region.

Person: 
- follow clean coding principles and better variable names

ChatGPT: 
- Certainly! Here's the `fig2words` function with cleaner variable names and adhering to clean coding principles:

```python
def number_to_words(number, region):
    # Dictionaries for number words
    indian_words = {
        0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
        10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
        17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
        60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
    }

    western_words = {
        0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
    }

    # Dictionary for scale names
    scale_names = {
        2: 'Hundred', 3: 'Thousand', 5: 'Lakh', 7: 'Crore', 6: 'Million', 9: 'Billion',
    }

    # Recursive function to convert number to words
    def convert_to_words(n, scale):
        if n == 0:
            return ''
        elif n < 20:
            return indian_words[n] if region == "I" else western_words[n]
        elif n < 100:
            return indian_words[(n // 10) * 10] + ' ' + convert_to_words(n % 10, scale)
        else:
            return indian_words[n // scale] + ' ' + scale_names[scale] + ' ' + convert_to_words(n % scale, scale)

    if region == "I":
        scale_factor = 100
        final_scale = 10000000  
    else:
        scale_factor = 1000
        final_scale = 1000000  

    words = convert_to_words(number // final_scale, scale_factor)
    remainder = convert_to_words(number % final_scale, scale_factor)

    if remainder:
        if region == "I":
            words += ' Crore ' if number // final_scale > 1 else ' Crore'
        else:
            words += ' Million ' if number // final_scale > 1 else ' Million'

        words += remainder

    return words
```



This version of the function uses more descriptive variable names and adheres to Python's naming conventions. Additionally, it maintains the recursive approach for converting numbers to words and is structured for readability and maintainability.
