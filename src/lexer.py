"""Implantação do analisador léxico."""

import ply.lex

import errors


@ply.lex.TOKEN(r"\n+")
def t_ignore_newline(token):
    """Conto o número de linhas."""
    token.lexer.lineno += token.value.count("\n")


def lexer():
    """Cria o objeto do analisador léxico."""
    return ply.lex.lex()


import ply.lex as lex

reserved = {
    'program': 'DIR_PROGRAM',
    'var': 'DIR_VAR',
    'procedure': 'DIR_PROC',
    'function': 'DIR_FUNC',
    'begin': 'DIR_BEGIN',
    'end': 'DIR_END',
    'type': 'DIR_TYPE',
    'of': 'DIR_OF',
    'const': 'DIR_CONST',
    'with': 'DIR_WITH',
    'if': 'STMT_IF',
    'then': 'STMT_THEN',
    'else': 'STMT_ELSE',
    'while': 'STMT_WHILE',
    'repeat': 'STMT_REPEAT',
    'for': 'STMT_FOR',
    'do': 'STMT_DO',
    'until': 'STMT_UNTIL',
    'to': 'STMT_TO',
    'downto': 'STMT_DOWNTO',
    'case': 'STMT_CASE',
    'array': 'TYPE_ARRAY',
    'set': 'TYPE_SET',
    'record': 'TYPE_RECORD',
    'file': 'TYPE_FILE',
    'integer': 'TYPE_INT',
    'real': 'TYPE_REAL',
    'character': 'TYPE_CHAR',
    'boolean': 'TYPE_BOOL',
    'string': 'TYPE_STRING',
    'read': 'FN_READ',
    'readln': 'FN_READLN',
    'write': 'FN_WRITE',
    'writeln': 'FN_WRITELN',
    'nil': 'OP_NIL',
}

# Lista de tokens
tokens = [
    'ID',
    'LIT_INT',
    'LIT_REAL',
    'LIT_STRING',
    'OP_ATRIB',
    'OP_SUM',
    'OP_MUL',
    'OP_REL',
    'OP_RANGE',
    'OP_OPAR',
    'OP_CPAR',
    'OP_OBRA',
    'OP_CBRA',
    'OP_COMMA',
    'OP_EOC',
    'OP_PERIOD',
    'OP_COLON',
    'COMMENT',
    'OP_ERROR',  # Token para identificar erros léxicos
] + list(reserved.values())

# Definição das regras para os tokens
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

def t_error(t):
    raise Exception(f"Erro léxico: caracter '{t.value[0]}' inválido na linha {t.lineno}, posição {t.lexpos + 1}")
    t.lexer.skip(1)
# Construção do lexer
lexer = lex.lex()

# # Função para testar o lexer
def test_lexer(input_text):
    lexer.input(input_text)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Exemplo de uso
if __name__ == "__main__":
    input_text = 'testando um texto 1 qu4l1r'
    test_lexer(input_text)

