%{
#include <stdio.h>
#include <stdlib.h>

// Declaraciones externas
extern int yylex(void);
extern int yylval;
int yyerror(char *s);
%}

%token NUMBER BOOL
%token AND OR NOT
%left OR
%left AND
%left '+' '-'
%left '*' '/'
%right NOT
%right UMINUS

%%

input: /* vacío */
     | input expr '\n' { printf("Expresión válida\n"); }
     | input error '\n' { 
         yyerror("Expresión inválida"); 
         yyerrok;
     }
     ;

expr: expr '+' term
    | expr '-' term
    | term
    ;

term: term '*' factor
    | term '/' factor
    | factor
    ;

factor: '(' expr ')'
      | logical_expr
      ;

logical_expr: logical_expr OR logical_term
           | logical_term
           ;

logical_term: logical_term AND logical_factor
           | logical_factor
           ;

logical_factor: NOT logical_factor
             | BOOL
             | NUMBER
             | '(' expr ')'
             ;

%%

int yyerror(char *s) {
    fprintf(stderr, "%s\n", s);
    return 0;
}

int main(void) {
    return yyparse();
}
