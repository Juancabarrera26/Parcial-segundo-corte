grammar CRUDSimple;

programa: instruccion+ ;

instruccion
    : insertar
    | consultar
    | modificar
    | borrar
    ;

insertar: 'INSERTAR' ID '(' campos ')' ;

consultar: 'CONSULTAR' ID condicion ;

modificar: 'MODIFICAR' ID condicion '(' campos ')' ;

borrar: 'BORRAR' ID condicion ;

campos: campo (';' campo)* ;

campo: ID '=' valor ;

condicion: 'DONDE' ID op valor ;

op: '=' | '!=' | '<' | '>' ;

valor: NUM | STRING ;

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
STRING: '"' (~["])* '"' ;

WS: [ \t\n\r]+ -> skip ;
