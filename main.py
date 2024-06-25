
def main():
  book = "frankenstein"
  with open("books/" + book + ".txt") as f:
    file_contents = f.read()
    dict = charCount(file_contents, wordCount(file_contents))
    report(book, dict, wordCount(file_contents))


def wordCount(text):
  words = text.split()
  count = 0

  for word in words: 
    count += 1
  return count







def sort_on(dict):
  return dict["num"]



def report(book, dict, count):
  list = []

  for key in dict:
    if key.isalpha():
      list.append({"letter": key , "num": dict[key]})

  print(f"--- Begin report of books/{book}.txt ---")
  print(f"{count} words found in the document")
  print()

  list.sort(reverse=True, key=sort_on)

  for x in range(0, len(list)):
    print(f"The '{list[x]['letter']}' character was found {list[x]['num']} times")

  print("--- End report ---")












def charCount(text, count):
  dict = {}
  # A list that contains all the words
  words = text.split()
  for x in range(0, count):
    characters = words[x].split()
    word = characters[0]
    #for c in range(0, len(characters[0])):
    for c in range(0, len(word)):
      letter = word[c].lower()

      if letter in dict:
        dict[letter] += 1
      else:
        dict[letter] = 1
    
  return dict



















main()