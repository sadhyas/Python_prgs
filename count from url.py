import requests

def download_file(url):
    response = requests.get(url)
    return response.text

def count_word(text, word):
    words = text.split()
    return words.count(word)

# Download the file and count the word
text = download_file('https://www.gutenberg.org/cache/epub/1513/pg1513.txt')
count = count_word(text, 'William',)

print(f"The word 'William' occurs {count} times in the text.")
