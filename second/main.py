from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    interpreter = Interpreter()
    while True:
        try:
            text = input('Input:')
            if text.lower() == "exit":
                print("Exiting...")
                break
            result = interpreter.interpret(text)
            print(result)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
