from lexer import TokenType, ParsingError, tokenPriority

class AST:
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Parser:

    def __init__(self):
        self.current_token = None
        self.lexer = None

    def __error(self):
        raise ParsingError("Lexical analysis error")

    def __eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.__error()

    def __term(self):
        token = self.current_token
        self.__eat(TokenType.INTEGER)
        return Num(token)

    def expr(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

        output = []
        operators = []

        while self.current_token.type != TokenType.EOF:
            if self.current_token.type == TokenType.INTEGER:
                output.append(self.current_token)
                self.__eat(TokenType.INTEGER)
            elif self.current_token.type in (TokenType.PLUS, TokenType.MINUS, TokenType.MUL, TokenType.DIV):
                while operators and operators[-1].type != TokenType.LPAREN and  tokenPriority(operators[-1].type) <= tokenPriority(self.current_token.type):
                    output.append(operators.pop())
                operators.append(self.current_token)
                self.__eat(self.current_token.type)
            elif self.current_token.type == TokenType.LPAREN:
                operators.append(self.current_token)
                self.__eat(self.current_token.type)
            elif self.current_token.type == TokenType.RPAREN:
                while operators and operators[-1].type != TokenType.LPAREN:
                    output.append(operators.pop())
                operators.pop()
                self.__eat(self.current_token.type)

        while operators:
            output.append(operators.pop())

        tree = self.build_tree(output)

        return tree

    @staticmethod
    def build_tree(output):
        stack = []
        for token in output:
            if token.type == TokenType.INTEGER:
                stack.append(Num(token))
            elif token.type in (TokenType.PLUS, TokenType.MINUS, TokenType.MUL, TokenType.DIV):
                right = stack.pop()
                left = stack.pop()
                stack.append(BinOp(left, token, right))
        return stack[0]