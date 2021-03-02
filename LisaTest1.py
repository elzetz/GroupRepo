mylist = []


def new_word(list):  # this func is taking list as param and input some new values into it
    new_input = (int(input()))
    if new_input == 0:
        return list
    else:
        list.append(new_input)
        return new_word(list)


