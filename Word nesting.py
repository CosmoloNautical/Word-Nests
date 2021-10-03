"""
A word nest is created by taking a starting word, and generating a new string by placing the word inside itself.
This process is then repeated several times.
This program can both nest and unnest a given word
"""

def nester():
    start_word = str(input("Enter the starting word\n"))
    current_word = start_word
    nest_depth = int(input("How many times should the word be nested?\n"))
    for x in range(0, nest_depth):
        midpoint = len(current_word) // 2
        current_word = current_word[:midpoint] + start_word + current_word[midpoint:]
        print(f"Depth {x + 1}:{current_word}")


def unnester():
    depth = 0

    def reccur_unnest(word_nest, nested_word, depth):
        if word_nest == nested_word:
            return True
        else:
            if word_nest.find(nested_word) != -1:
                depth += 1
                word_nest = word_nest.replace(nested_word, "")
                print(f"Depth {depth}:{word_nest}")
                return reccur_unnest(word_nest, nested_word, depth)
            else:
                return False

    word_nest = str(input("Enter the word nest\n"))
    nested_word = str(input("Enter the word that is nested\n"))
    return reccur_unnest(word_nest, nested_word, depth)
