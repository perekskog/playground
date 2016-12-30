import sys
import json


def fetch_items(filein):
    movies = list()
    with open(filein, 'r', encoding='utf-8') as f:
        for row in f:
            # file = [ comment | movie ]*
            # comment = # string
            # movie = disk TAB title_with_attributes
            # title_with_attributes =  title TAB attributes
            # attributes = *format | COMMA § category | COMMA # language | COMMA & mirrored_on_mediaserver
            # title = string [string SPACE]*
            # language = audio SLASH subtitle
            # mirrored_on_mediaserver = & ms

            # comment
            if row[0] == "#":
                print("continue 1")
                continue

            # wanted
            if row.find("§wanted") > -1:
                print("continue 2")
                continue

            print(">"+row.strip("\n)"))

            # disk, title, attributes
            tokens = row.split("\t")
            disk = ""
            title = ""
            attributes = ""
            if len(tokens) >=1:
                disk = tokens[0].strip("\n")
            if len(tokens) >= 2:
                title = tokens[1].strip("\n")
            if len(tokens) >= 3:
                attributes = tokens[2].strip("\n")
            print("disk=[{}], title=[{}]".format(disk, title))


            # attributes
            attr = attributes.split(",")
            media = ""
            lang = ""
            category = []
            mediaserver = False
            for i in attr:
                #print("<<{}>>".format(i))
                i = i.strip(" ").strip("\n")
                if len(i)==0:
                    continue
                if i.find("*") >= 0:
                    media = i
                if i.find("#") >= 0:
                    lang = i
                if i.find("§") >= 0:
                    category.append(i)
                if i.find("&ms") >= 0:
                    mediaserver = True
            print("\tmedia=[{}], lang=[{}], cat={}, ms=[{}]".format(media, lang, category, mediaserver))

    return movies


def main(filein, fileout):
    items = fetch_items(filein)
#    open(fileout, 'wb').write(json.dumps(items, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8'))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])