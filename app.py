import os,sys,warnings
import ply.lex as lex
import ply.yacc as yacc

line_number = 0 #use for labaling

if __name__ == "__main__":
    
    tokens = [
        'PROGRAM' ,
        'VAR' ,
        'INT',
        'REAL' ,
        'BEGIN' ,
        'END' ,
        'IF' ,
        'THEN' ,
        'ELSE' ,
        'WHILE' ,
        'DO' ,
        'PRINT' ,
        'PLUS' ,
        'MINUS' ,
        'UMINUS' ,
        'MUL' ,
        'DIV' ,
        'NEG' ,
        'MOD' ,
        'EQL' ,
        'NEQL' ,
        'SEMICOLON' ,
        'COLON' ,
        'COMMA' ,
        'ASSIGN' ,
        'LT' ,
        'GT' ,
        'LE' ,
        'GE' ,
        'AND' ,
        'OR' ,
        'NOT' ,
        'IDENTIFIER',
        'LPAREN' ,
        'RPAREN',
        'NUMBER',
    ]

    precedence = (
        (('right' , 'MINUS') , ('right' , 'PLUS') ,  ('right' , 'DIV') , ('right' , 'MUL') , ('right' , 'UMINUS') , ('right' , 'IF'))
    )

    def t_PROGRAM(t):
        r'[p][r][o][g][r][a][m]'
        t.value = t.value
        return t

    def t_VAR(t):
        r'[v][a][r]'
        t.value = t.value
        return t

    def t_BEGIN(t):
        r'[b][e][g][i][n]'
        t.value = t.value
        return t

    def t_END(t):
        r'[e][n][d]'
        t.value = t.value
        return t

    def t_IF(t):
        r'[i][f]'
        t.value = t.value
        return t

    def t_THEN(t):
        r'[t][h][e][n]'
        t.value = t.value
        return t

    def t_ELSE(t):
        r'[e][l][s][e]'
        t.value = t.value
        return t

    def t_WHILE(t):
        r'[w][h][i][l][e]'
        t.value = t.value
        return t

    def t_DO(t):
        r'[d][o]'
        t.value = t.value
        return t

    def t_PRINT(t):
        r'[p][r][i][n][t]'
        t.value = t.value
        return t

    def t_INT(t):
        r'\d+'
        t.value = str(t.value)
        return t

    def t_PLUS(t):
        r'\+'
        t.value = t.value
        return t

    def t_UMINUS(t):
        r'[u][-]'
        t.value = t.value
        return t

    def t_MINUS(t):
        r'-'
        t.value = t.value
        return t

    def t_MUL(t):
        r'\*'
        t.value = t.value
        return t

    def t_DIV(t):
        r'\+'
        t.value = t.value
        return t

    def t_MOD(t):
        r'[m][o][d]'
        t.value = t.value
        return t

    def t_ASSIGN(t):
        r'[:][=]'
        t.value = t.value
        return t

    def t_EQL(t):
        r'='
        t.value = t.value
        return t

    def t_NEQL(t):
        r'[<][>]'
        t.value = t.value
        return t

    def t_SEMICOLON(t):
        r'[;]'
        t.value = t.value
        return t

    def t_COLON(t):
        r'[:]'
        t.value = t.value
        return t

    def t_LE(t):
        r'[<][=]'
        t.value = t.value
        return t

    def t_GE(t):
        r'[>][=]'
        t.value = t.value
        return t


    def t_LT(t):
        r'[<]'
        t.value = t.value
        return t


    def t_GT(t):
        r'[>]'
        t.value = t.value
        return t

    def t_AND(t):
        r'[a][n][d]'
        t.value = t.value
        return t

    def t_OR(t):
        r'[o][r]'
        t.value = t.value
        return t

    def t_NOT(t):
        r'[n][o][t]'
        t.value = t.value
        return t
    
    def t_LPAREN(t):
        r'[(]'
        t.value = t.value
        return t

    def t_COMMA(t):
        r'[,]'
        t.value = t.value
        return t

    def t_RPAREN(t):
        r'[)]'
        t.value = t.value
        return t
    
    def t_IDENTIFIER(t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.value = t.value
        return t

    
    #handle error for undefined character
    def t_error(t):
        print("undefined characters: ", t.value)
        t.lexer.skip(1)

    t_ignore = ' \t\n' 

    def p_program(p):
        '''program_p : PROGRAM  declarations compound_statement'''
        p[0] = '#include <stdio.h>\n' + p[3] + 'int main() \n {\n' + p[4] + '\n}'
        print(p[0])

    def p_declarationsVar(p):
        '''declarations : VAR declarion_list '''
        p[0] = p[2]
        print(p[0])

    def p_declarations(p):
        '''declarations : '''
        p[0] = ''
        print(p[0])

    def p_declarionList(p):
        '''declarion_list : identifier_list COLON type'''
        p[0] = p[3] + ' ' + p[1]
        print(p[0])

    def p_declarionListNested(p):
        '''declarion_list : declarion_list SEMICOLON identifier_list COLON type'''
        p[0] = p[1] + ';\n' + p[5] + ' ' + p[3]
        print(p[0])
    
    def p_identifierList(p):
        '''identifier_list : IDENTIFIER'''
        p[0] = p[1]
        print(p[0])

    def p_identifierListNested(p):
        '''identifier_list : identifier_list COMMA IDENTIFIER'''
        p[0] = p[1] + ',' + p[3]
        print(p[0])

    def p_type(p):
        '''type : INT'''
        p[0] = p[1]
        print(p[0])

    def p_compoundsStatement(p):
        '''compound_statement : BEGIN statement_list END'''
        p[0] = 'begin\n' + p[2] + '\nend\n'
        print(p[0])

    def p_statementList(p):
        '''statement_list : statement'''
        p[0] = p[1]
        print(p[0])

    def p_statementListNested(p):
        '''statement_list : statement_list SEMICOLON statement'''
        p[0] = p[1] + ';\n' + p[3]
        print(p[0])

    def p_statement(p):
        '''statement : IDENTIFIER ASSIGN expression'''
        p[0] = p[1] + '=' + p[3]
        print(p[0])

    def p_statementWithElse(p):
        '''statement : IF expression THEN statement ELSE statement'''
        global line_number
        p[0] = 'if(' + p[2] + ')' + ' goto label' + str(line_number) + '\n' + p[6] + '\ngoto label' + str(line_number + 1) + '\nlabel' + str(line_number) + ':' + p[4] + '\nlabel' + str(line_number + 1) + ':'
        line_number = line_number + 2

    def p_statementWithoutElse(p):
        '''statement : IF expression THEN statement'''
        global line_number
        p[0] = 'if(' + p[2] + ')' + ' goto label' + str(line_number) + '\ngoto label' + str(line_number + 1) + '\nlabel' + str(line_number) + ':' + p[4] + '\nlabel' + ':'
        line_number = line_number + 2
    def p_statementLoop(p):
        '''statement : WHILE expression DO statement'''
        p[0] = 'label' + str(line_number) + ':if(' + p[2] + ')' + ' goto label' + str(line_number + 1) + '\ngoto' + str(line_number + 2) + '\nlabel' + str(line_number + 1) + ':' + p[4] + '\ngoto' + str(line_number) + '\nlabel' + str(line_number + 2) + ':'

    def p_statementComp(p):
        '''statement : compound_statement'''
        p[0] = p[1]
        print(p[0])

    def p_statementPrint(p):
        '''statement : PRINT LPAREN expression RPAREN'''
        p[0] = 'print(' + p[2] + ')'
        print(p[0])

    def p_expression(p):
        '''int_expression : INT'''
        p[0] = p[1]
        print(p[0])

    def p_expressionid(p):
        '''expression : IDENTIFIER'''
        p[0] = p[1]
        print(p[0])

    def p_expressionPlus(p):
        '''int_expression : int_expression PLUS int_expression'''
        p[0] = p[1] + '+' + p[3]
        print(p[0])

    def p_expressionMinus(p):
        '''int_expression : int_expression MINUS int_expression'''
        p[0] = p[1] + '-' + p[3]
        print(p[0])

    def p_expressionMul(p):
        '''int_expression : int_expression MUL int_expression'''
        p[0] = p[1] + '*' + p[3]
        print(p[0])

    def p_expressionDiv(p):
        '''int_expression : int_expression DIV int_expression'''
        p[0] = p[1] + '/' + p[3]
        print(p[0])

    def p_expressionMod(p):
        '''int_expression : int_expression MOD int_expression'''
        p[0] = p[1] + '%' + p[3]
        

    def p_expressionUminus(p):
        '''int_expression : UMINUS int_expression'''
        p[0] = '-1 * (' + p[2] + ')'

    def p_expressionLt(p):
        '''bool_expression : int_expression LT int_expression'''
        p[0] = p[1] + '<' + p[3]

    def p_expressionEql(p):
        '''bool_expression : int_expression EQL int_expression'''
        p[0] = p[1] + '==' + p[3]

    def p_expressionGt(p):
        '''bool_expression : int_expression GT int_expression'''
        p[0] = p[1] + '>' + p[3]

    def p_expressionNeql(p):
        '''bool_expression : int_expression NEQL int_expression'''
        p[0] = p[1] + '!=' + p[3]

    def p_expressionLe(p):
        '''bool_expression : int_expression LE int_expression'''
        p[0] = p[1] + '<=' + p[3]

    def p_expressionGe(p):
        '''bool_expression : int_expression GE int_expression'''
        p[0] = p[1] + '>=' + p[3]

    def p_expressionAnd(p):
        '''bool_expression : bool_expression AND bool_expression'''
        p[0] = p[1] + '&&' + p[3]

    def p_expressionOr(p):
        '''bool_expression : bool_expression OR bool_expression'''
        p[0] = p[1] + '||' + p[3]

    def p_expressionNot(p):
        '''bool_expression : NOT bool_expression'''
        p[0] = '~' + p[2]

    def p_expressionParen(p):
        '''expression : LPAREN expression RPAREN'''
        p[0] = '(' + p[2] + ')'

    def p_expressionBool(p):
        '''expression : bool_expression'''
        p[0] = p[1]

    def p_expressionInt(p):
        '''expression : int_expression'''
        p[0] = p[1]


print("start C compiler")

data = """program test_if
var 
 no, result : int
begin
  no := 0;
  if (no > 0) then
   result := 1
  else
    if (no < 0) then
     result := 2
    else
      if (no = 0) then
      result := 3;
  print(result)
end"""

lex.lex()
lex.input(data)
parser = yacc.yacc()
parser.parse(data)
while 1:
    token = lex.token()
    if not token:
        break
    print(token)


