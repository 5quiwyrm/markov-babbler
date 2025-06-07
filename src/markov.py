import random as r

def generate_data(corpuspath: str, depth: int) -> str:
  with open(corpuspath, 'r', encoding = "utf-8") as corpusfile:
    corpus = corpusfile.read(int(1e7))
    if len(corpus) < depth:
      print("your corpus is too short (thats what she said)")
      raise
    data = {}
    gram = corpus[0:depth]
    i = 0
    a = 0
    for ch in corpus[depth:]:
      if a + 0.05 < (i / (len(corpus) - depth)):
        print(f"progress: ({a / 0.05} / {1 / 0.05}) {i} / {len(corpus) - depth}")
        a += 0.05
      i += 1
      if gram not in data:
        data.update({gram: {}})
      if ch not in data[gram]:
        data[gram].update({ch: 1})
      else:
        data[gram].update({ch: data[gram][ch] + 1})
      gram = gram[1:] + ch
    data_ser = [
      [
        grm,
        [
          [
            key,
            data[grm][key]
          ]
          for key in data[grm].keys()
        ]
      ]
      for grm in data.keys()
    ]
    for (_, lis) in data_ser:
      total = sum(a[1] for a in lis);
      lis.sort()
      for i in lis:
        i[1] /= total
    return dict(data_ser)

def get_next(gram: str, data: dict[list]) -> str:
  if gram not in data:
    raise
  else:
    subdata = data[gram]
    rand = r.random()
    acc = 0
    for [ch, freq] in subdata:
      if acc + freq >= rand:
        return ch
      else:
        acc += freq
    return subdata[-1][0]

def get_next_n(start: str, data: dict[list], n: int) -> str:
  grm = start
  ret = grm
  for _ in range(n):
    try:
      ret += get_next(grm, data)
      grm = ret[-len(grm):]
    except:
      return ret
  return ret

