print("L.CHRISTINA SHERIN")
print("URK19CS11063")
print("..............")
i = open("Input.txt",'r').readlines()
op = open("Optab.txt",'r').readlines()
s = open("Symtab.txt",'r').readlines()
output = open('Output.txt','w')
optab = {};
l = []
m = []
n = []
a = []
 
opcode = []
object_code = []
 
for line in op:
  op = line.split()
  optab.update({op[0]: op[1]})
for line in i:
  if "START" in line:
    start = line.split()[2]
    x = int(start, 16)
    a.append('')
  else:
    a.append(str(hex(x)[2:]))
    x += 3
 
for line in i:
  line = line.split()
  if len(line) == 3:
    l.append(line[0])
    m.append(line[1])
    n.append(line[2])
  elif len(line) == 2:
    l.append('')
    m.append(line[0])
    n.append(line[1])
  else:
    m.append(line[0])
for i in m:
  if i == "START":
    continue;
  if i in optab:
    x = str(optab[i])
    y = str(a[l.index(n[m.index(i)])])
    object_code.append('^' + str(x + y))
 
ob = ''.join(object_code)
leng = len(object_code)
x = str(hex(leng * 3)[1:])
if 'x' in x:
  x = x.replace('x','0')
 
output.write('H^' + l[0] + '^' + '00' + a[1] + '^' + '0000' + a[len(a) - 1][2:]+ '\n')
output.write('T^' + a[1] + '^' + x + ob+'\n')
output.write('E^' + '00' + a[1]+'\n')
output.close()
 
print(open('output.txt').read())
