import sys
import re
import json

keys = []
values = []
Dictionary = {}

def solve_Phrase(Phrase):

    if(len(Phrase) == 2):
        return Phrase

    Phrase[0] = Phrase[0] + '_' + Phrase[1]
    Phrase.pop(1)
    return solve_Phrase(Phrase)

def main():
    
    sent_file = open(sys.argv[1]) #Dictionary
    tweet_file = open(sys.argv[2]) #JsonData

    f = open('data.json', mode='r')
    js_data = json.load(f)

    line = sent_file.readline()
    while line != '':
        sep = line.strip()
        sep = re.split(r'[\s+\t]', sep)
        
        if(len(sep) >= 3):
            sep = solve_Phrase(sep)

        keys.append(str.lower(sep[0]))
        values.append(int(sep[1]))
        line = sent_file.readline()

    Dictionary = dict(zip(keys,values))

    #讀檔
    json_data = json.load(tweet_file)
    if json_data['full_text'] != '':
        sep = json_data['full_text'].split(' ')

        score = 0
        for item in sep:
            
            item = re.sub('[^a-zA-Z]', '', item)
            if(item == ''):
                continue

            try:
                score += Dictionary[str.lower(item)]
                print('Match: '+ item)
            except Exception:
                pass

        print("mood score : %d" %score)

    else:
        print('No Score')


if __name__ == '__main__':
    main()
