cpu = bytearray([0x00]*32767)

code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
scani = 0
scanstr = ""

def scan():
    global scani
    global scanstr
    if scani >= len(scanstr):
        scanstr = input()
        scani = 0
    scani += 1    
    return scanstr[scani-1]
    

def clear():
    global cpu
    global scanstr
    global scani
    cpu = bytearray([0x00]*32767)
    scanstr = ""
    scani = 0
   
def main():
    clear()
    source = ""
    for i in code:
        if i in ['+', '-', '<', '>', '.', ',', '[', ']']: source += i
    j = 0
    brc = 0
    i = 0
    while i < len(source):
        if source[i] == '>': j += 1
        if source[i] == '<': j -= 1
        if source[i] == '+': cpu[j] = (cpu[j] + 1 + 256) % 256
        if source[i] == '-': cpu[j] = (cpu[j] - 1 + 256) % 256
        if source[i] == '.': print(chr(cpu[j]),end='')
        if source[i] == ',': cpu[j] = ord(scan())
        if source[i] == '[':
            if not cpu[j]:
                brc += 1
                while brc:
                    i += 1
                    if source[i] == '[': brc -= 1
                    if source[i] == ']': brc += 1
            else:
                i += 1
                continue
        elif source[i] == ']':
            if not cpu[j]:
                i += 1
                continue
            else:
                if source[i] == ']': brc += 1
                while brc:
                    i -= 1
                    if source[i] == '[': brc -= 1
                    if source[i] == ']': brc += 1
                i -= 1
        i += 1
    
