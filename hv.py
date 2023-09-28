with open("horz.txt","r") as file:
    red = file.read()

ouput = []

for red in lines:
    a = line.split()
    ouput.append(a)


s = list(zip(*ouput))
c = []


for t in s:
    c.append("\t".join(t))

with open("vert.txt", 'w') as file:
    file.write("\n".join(c))
    
