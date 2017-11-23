import sys


def my_get_opt(argv):
    assert "--s" in argv, ("неправильный ввод введите повторно"
                           " с аргументом --help")
    dict_arg = {"--s": None, "--i": None, "--b": None, "--f": None}
    for a in argv:
        assert a in dict_arg, "ошибка имени аргумента {}".format(a)
        value_index = argv.index(a) + 1
        if a in "--help":
            return ("python <filename> --s <string> [--help]"
                    " [--i <integer>>] [--f <float>] [--b <bool>]")
        elif a in dict_arg and "--" not in argv[value_index]:
            if "s" in a[-1]:
                dict_arg[a] = argv.pop(value_index)
            elif "i" in a[-1]:
                dict_arg[a] = int(argv.pop(value_index))
            elif "f" in a[-1]:
                dict_arg[a] = float(argv.pop(value_index))
            elif "b" in a[-1]:
                dict_arg[a] = bool(argv.pop(value_index))
    return dict_arg


if __name__ == '__main__':
    print(my_get_opt(sys.argv[1:]))
