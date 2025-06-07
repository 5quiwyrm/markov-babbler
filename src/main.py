
import markov

if __name__ != "__main__":
  raise Exception("This is not the main one (thats what she said)")

corpus = input("which corpus? ")
data = markov.generate_data(f"./corpora/{corpus}.txt", 8)

n = int(input("how many chars? "))
text = markov.get_next_n(list(data.keys())[0], data, n)
print(text)


