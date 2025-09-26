import sys


def read_file(file: str) -> None:
    """Receives a file name as an argument from the command line (type: str), opens it and prints it's content on the terminal. Conversion errors are treated with Exceptions"""
    try:
        with open(file, "r+", encoding="utf-8") as f:
            for line in f:
                print(line, end="")
            f.close()
    except FileNotFoundError:
        print("Erro: arquivo não encontrado")
    except IsADirectoryError:
        print("Erro: o argumento enviado é um diretório")
    except Exception as e:
        print(f"Erro inesperado: {type(e).__name__}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        read_file(sys.argv[1])
    else:
        print("Erro: nenhum argumento foi passado")


# Bare Except: A bare except catches BaseException which includes KeyboardInterrupt, SystemExit, Exception, and others. Catching BaseException will ignore KeyBoardInterrupt for example, which can make it hard to interrupt the program (e.g., with Ctrl-C) and can disguise other problems.

# type(e): returns the type/class of the "e" object. e.g.: <class 'ValueError'>, <class 'int'>

# .__name__: it's an attribute that contains the class' name as a str (removes <class ''> and returns only the name)