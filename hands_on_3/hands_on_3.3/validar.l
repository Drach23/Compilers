%{
#include "validar.tab.h"
#include <stdlib.h>
#include <string.h>

// Declaraciones externas
extern int yylval;
%}

%%
[0-9]+ { yylval = atoi(yytext); return NUMBER; }
[ \t] ;
[\n] { return '\n'; }
[+\-*/()] { return yytext[0]; }
"AND" { return AND; }
"OR" { return OR; }
"NOT" { return NOT; }
"TRUE"|"FALSE" { yylval = strcmp(yytext, "TRUE") == 0 ? 1 : 0; return BOOL; }
. { return yytext[0]; }
%%