



def LinesToFile(lines, path):
  f = open(path, "w")
  for l in lines:
    f.write(l)


def FileToLines(path):
  lines = []
  
  f = open(path, "r")
  for l in f:
    lines.append(l)
  
  return lines
