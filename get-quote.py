import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 17
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  print(quotes[rnd],quotes[rnd2])

if __name__== "__main__":
  primary()
