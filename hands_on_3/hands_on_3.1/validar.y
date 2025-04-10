%{
#include <stdio.h>
#include <stdlib.h>

// Declaraciones externas
extern int yylex(void);
extern int yylval;
int yyerror(char *s);  // Declarar la función yyerror aquí
%}

%token NUMBER
%left '+' '-'
%left '*' '/'
%right UMINUS

%%

input: /* vacío */ { printf("Listo para procesar expresiones\n"); }
     | input expr '\n' { printf("Expresión válida\n"); }
     | input error '\n' { 
         yyerror("Expresión inválida"); 
         yyerrok;
         printf("Puede continuar ingresando expresiones\n");
     }
     ;

expr: expr '+' expr { printf("Suma detectada\n"); }
    | expr '-' expr { printf("Resta detectada\n"); }
    | expr '*' expr { printf("Multiplicación detectada\n"); }
    | expr '/' expr { printf("División detectada\n"); }
    | '-' expr %prec UMINUS { printf("Negación detectada\n"); }
    | '(' expr ')' { printf("Paréntesis detectado\n"); }
    | NUMBER { printf("Número %d detectado\n", yylval); }
    ;

%%

// Definición de la función yyerror aquí, después de las reglas
int yyerror(char *s) {
    fprintf(stderr, "%s\n", s);
    return 0;
}

int main(void) {
    return yyparse();
}
