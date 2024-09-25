grammar hm;


root    : declarations expr? EOF
        ;


declarations    : (left_value '::' ty)*
                ;


left_value      : LSTRING
                | INTVAL
                | OPERATOR
                ;


ty              : simple_type                                   # uniType
                | simple_type '->' ty                           # multiType
                ;


simple_type     : (LSTRING | USTRING)                           # sType 
                | '(' (LSTRING | USTRING) '->' simple_type ')'  # cType
                ;


expr            : left_value                                    #value
                | expr expr                                     #aplication
                | '\\' left_value '->' expr                     #abstraction
                | '(' expr ')'                                  #par
                ;




/*---------------Arithmetic operands---------------*/

OPERATOR : '(' ([!-/:-@^] | '&&') ')' ;


/*---------------Type values---------------*/

INTVAL  : [0-9]+ ;
USTRING : [A-Z]+ ;
LSTRING : [a-z]+ ;


/*---------------Other---------------*/

WS      : [ \t\n\r]+ -> skip ;