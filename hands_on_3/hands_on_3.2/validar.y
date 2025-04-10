%{
#include <stdio.h>
#include <stdlib.h>

// Declaraciones externas
extern int yylex(void);
extern int yylval;
void yyerror(const char *s);  // Declarar la función yyerror aquí
%}

%token BOOLEAN
%token AND OR NOT

%%

input: /* vacío */ { printf("Listo para procesar expresiones\n"); }
     | input expr '\n' { printf("Expresión válida\n"); }
     | input error '\n' { 
         yyerror("Expresión inválida"); 
         yyerrok;
         printf("Puede continuar ingresando expresiones\n");
     }
     ;

expr: expr AND term
    | expr OR term
    | term
    ;

term: NOT factor
    | factor
    ;

factor: '(' expr ')'
      | BOOLEAN
      ;

%%

// Definición de la función yyerror aquí, después de las reglas
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(void) {
    if (yyparse() == 0) {
        printf("Expresión válida\n");
    } else {
        printf("Expresión inválida\n");
    }
    return 0;
}
