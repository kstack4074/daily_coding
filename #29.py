'''

'''
def run_length_encoder(string):
    encodedString = ''
    count = 0

    for idx, letter in enumerate(string, start = 1):
        if letter == string[idx:idx + 1]:
            count += 1
        else:
            count += 1
            encodedString += (str(count) + letter)
            count = 0

    return encodedString


def run_length_decoder(string):
    #Assuming correct formatting
    #Then always contain even number of elemnents

    decodedString = []
    for idx in range(0, len(string), 2):
        letter = string[idx + 1:idx + 2]
        number = string[idx:idx + 1]

        decodedString += [letter for _ in range(int(number))]

    print(''.join(decodedString))

if __name__ == '__main__':
    string = "AAAABBBCCDA"
    encoded = run_length_encoder(string)
    print(encoded)
    decoded = run_length_decoder(encoded)
    print(decoded)
