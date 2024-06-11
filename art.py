import random

# Define the ASCII art for the text
text_art = r"""
  ____        _   _                 
 |  _ \ _   _| |_| |__   ___  _ __  
 | |_) | | | | __| '_ \ / _ \| '_ \ 
 |  __/| |_| | |_| | | | (_) | | | |
 |_|    \__, |\__|_| |_|\___/|_| |_|
        |___/                       
"""

# Define the ASCII art for the cat
cat_art = r"""
 /\_/\  
( o.o ) 
 > ^ <
"""

def insert_cat_randomly(text_art, cat_art):
    text_lines = text_art.split('\n')
    cat_lines = cat_art.split('\n')

    max_text_width = max(len(line) for line in text_lines)
    max_cat_width = max(len(line) for line in cat_lines)

    # Calculate a random start position for the cat
    num_positions = len(text_lines) - len(cat_lines)
    start_position = random.randint(0, num_positions)

    # Combine text and cat art
    combined_art = []
    for i, line in enumerate(text_lines):
        if i >= start_position and i < start_position + len(cat_lines):
            cat_line = cat_lines[i - start_position]
            combined_line = line.ljust(max_text_width) + " " + cat_line
        else:
            combined_line = line
        combined_art.append(combined_line)

    return "\n".join(combined_art)

# Insert the cat randomly and print the result
#combined_art = insert_cat_randomly(text_art, cat_art)
#print(combined_art)

