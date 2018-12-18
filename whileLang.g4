grammar whileLang;            // Define a grammar called Hello


prog  : instr ;         // match keyword hello followed by an identifier

expr : LPAR expr RPAR
     | aexpr
     | CONS expr expr     //tuple
     | HD expr
     | TL expr
     | ISEQUAL expr expr
     ;

quote: LPAR quote RPAR
     | QUOTE a
     ;

var: LPAR var RPAR
   | VAR NUM
   ;

instr : LPAR instr RPAR
      | ATTR var expr
      | SEMICOLON instr instr
      | WHILE expr instr
      ;


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



aexpr: LPAR aexpr RPAR
     | quote
     | var
     | aexpr PLUS aexpr
     | aexpr MINUS aexpr
     | aexpr MULT aexpr
     ;

bexpr: TRUE
     | FALSE
     | aexpr EQUAL aexpr
     | aexpr SMALLER aexpr
     | aexpr BIGGER aexpr
     | MINUS bexpr
     | bexpr AND bexpr
     | bexpr OR bexpr
     ;

a: NUM | NIL;
NUM: DIGIT+;
NIL: 'nil';
// Whitespaces -> ignored
NEWLINE: '\r'? '\n'  -> skip ;
WS: [ \t]+ -> skip ;
fragment LETTER: 'A'..'Z' | 'a'..'z' ;
fragment DIGIT: '0'..'9' ;