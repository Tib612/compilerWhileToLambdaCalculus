grammar whileLang;            // Define a grammar called Hello

prog  : instr ;         // match keyword hello followed by an identifier

instr : LPAR instr RPAR
      | ATTR var expr
      | SEMICOLON instr instr
      | WHILE expr instr
      ;

expr : LPAR expr RPAR
     | CONS expr expr     //tuple
     | HD expr
     | TL expr
     | ISEQUAL expr expr
     | quote
     | var
     | expr PLUS expr
     | expr MINUS expr
     | expr MULT expr
     ;

quote: LPAR quote RPAR
     | QUOTE a
     ;

var: LPAR var RPAR
   | VAR NUM
   ;

a: NUM | NIL;

ATTR: ':=';
SEMICOLON: ';';
ISEQUAL: '=?';
WHILE: 'while';
VAR: 'var';
QUOTE: 'quote';
CONS: 'cons';
HD: 'hd';
TL: 'tl';
LPAR: '(';
RPAR: ')';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
TRUE: 'true';
FALSE: 'false';
EQUAL: '=';
SMALLER: '<';
BIGGER: '>';
AND: 'and';
OR: 'or';

NUM: DIGIT+;
NIL: 'nil';
// Whitespaces -> ignored
NEWLINE: '\r'? '\n'  -> skip ;
WS: [ \t]+ -> skip ;
fragment LETTER: 'A'..'Z' | 'a'..'z' ;
fragment DIGIT: '0'..'9' ;