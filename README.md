# Lexical Analyzer

In order to run the script you should have 3 files ready:
1.  Transition matrix json file
2.  Text input file
3.  The output json file

Call

    py lexical.py <transition-matrix-file> <input-string-file> <output-file-name>

Example:
    
    py lexical.py ./examples/test-transition-matrix.json ./examples/input-string.txt ./examples/out.json

Check out the `examples` directory to see how the transition matrix file is specified.

# Syntactic Analyzer 

In order to run the script successfully you should have 1 file ready:
-   Lexical Analyzer .json output file

Call

    py syntactic.py out.json

Output

    You will see in terminal whether the order of tokens is correct depending
    on the grammar:
        - True, meaning the syntax is correct
        - False, meaning the syntax has a violation