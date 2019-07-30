class Parser:

    def parse(self, text):
        # This method is the entry point for the language parser.
        # It receives a text in the parameter and returns an object
        # containing the model expressed in the text.
        # <pre:> the text is well formed with respect to the language
        #        syntax.
        print("I'm parsing " + text)
