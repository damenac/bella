grammar Bella;

/** A program is a list of instructions */
program: instruction instruction*;

instruction: up | down;

up: 'up' ID;

down: 'down' ID;

ID: [a-z]+;

WS: [ \t\r\n]+ -> skip;