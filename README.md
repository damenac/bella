# Bella

Bella is my cat :)
In this repo, I am exploring the construction of software languages in python. The grammar is written in antlr, the parser is generated in python. 

## Installing antlr as a module of the python distribution

pip install antlr4-python2-runtime

## Compiling the grammar

To compile the grammar and generate the language tooling, execute:

```
$ java -Xmx500M -cp /usr/local/lib/antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python2 Bella.g4
```

To compile a specific language script, execute:

```
$ python Bella.py
```

