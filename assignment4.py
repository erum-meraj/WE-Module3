import random
import re


def read_file(filename):
    """Read the text from the file."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def build_chain(text, chain_length):
    """Build a Markov chain based on the given text and chain length."""
    words = re.findall(r"\b\w+\b", text)
    chain = {}
    for i in range(len(words) - chain_length):
        prefix = tuple(words[i : i + chain_length])
        suffix = words[i + chain_length]
        if prefix in chain:
            chain[prefix].append(suffix)
        else:
            chain[prefix] = [suffix]
    return chain


def generate(filename, start_words, chain_length, num_generated):
    """Generate a sentence resembling the text in the file."""
    text = read_file(filename)
    chain = build_chain(text, chain_length)
    sentence = start_words[:]

    while len(sentence) < num_generated:
        current_prefix = tuple(sentence[-chain_length:])
        if current_prefix in chain:
            next_word = random.choice(chain[current_prefix])
            sentence.append(next_word)
        else:
            break

    return " ".join(sentence)


# Example usage:
filename = "test.txt"
start_words = ["The", "quick", "brown"]  # Example start words
chain_length = 2
num_generated = 20
generated_sentence = generate(filename, start_words, chain_length, num_generated)
print(generated_sentence)
