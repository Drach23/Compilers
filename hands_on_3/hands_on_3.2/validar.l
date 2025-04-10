%{
#include "validar.tab.h"
#include <stdlib.h>

// Declaraciones externas
extern int yylval;
%}

%%
[01] { yylval = atoi(yytext); return BOOLEAN; }
AND { return AND; }
OR { return OR; }
NOT { return NOT; }
[ \t] ;
[\n] { return '\n'; }
[()] { return yytext[0]; }
. { return yytext[0]; }
%%