import sys


def character(c):
    if ord(c) == 197:
        return "Å"
    if ord(c) == 196:
        return "Ä"
    if ord(c) == 214:
        return "Ö"
    if ord(c) == 229:
        return "å"
    if ord(c) == 228:
        return "ä"
    if ord(c) == 246:
        return "ö"
    if ord(c) == 167:
        return "§"
    if ord(c) > 127:
        return c
    return chr(ord(c))


def main(infile, outfile):
    fout = open(outfile, mode="w")
    with open(infile, mode="rb") as fin:
        for ch in iter(lambda: fin.read(1), ''):
            if len(ch) == 1:
                fout.write(character(ch))
                #print(character(ch), ord(ch))
                #print(ch)
            else:
                break



if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])