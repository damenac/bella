grammar Bella;

/** A program is a list of instructions */
program: instruction instruction*;

/** An instruction can be either 'up' or 'down' */
instruction: up | down;

up: 'up' NUMBER;

down: 'down' NUMBER;

ID: [a-z]+;

NUMBER: ('0' ..'9')+;

WS: [ \t\r\n]+ -> skip;