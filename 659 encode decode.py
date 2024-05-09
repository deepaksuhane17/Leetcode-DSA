def encode(word_list: list):

    res = ""
    for word in word_list:
        res += f"{len(word):04d}"
        res += word

    return res


def decode(input):

    res = []

    word_len = ""
    del_counter = 0
    next_i = 0

    for i in range(len(input)):
        
        if i<next_i:
            continue

        del_counter += 1
        word_len += input[i]

        if del_counter == 4:
            word_len = int(word_len)
            res.append(input[i + 1 : i + word_len + 1])
            next_i = i + word_len + 1
            del_counter = 0
            word_len = ""

    return res


print(decode(encode(["we", "say", ":", "yes"])))
