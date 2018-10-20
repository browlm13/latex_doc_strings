#!/usr/bin/env

__filename__ = "latex_doc_strings.py"
__author__ = "L.J. Brown"

import re
from IPython.display import display, Math, Latex

def extract_doc_latex(method):
    """
        looks for latex in doc strings of passes method.
        
        Format example for docstring:
        
            r\""" 
                    Foo Method Description 

                :latex: MULTI-LINE
                        LATEX EXPRESSION
                        INSERTED HERE
                        
                :param bar: (example parameter)
                :returns: (whatever) 

                * [Notes] : 
                
                    - latex code must be followed by 
                        at least one ':'(like the one 
                        leading param above)
                        
                    - doc string must be proceeded by r\""" 
            \"""
            
        :param: method with string literal doc string containing latex
        :returns: latex string literal
        
    """
    p = re.compile('(?:\:latex\:)([\s\S]+?)(?:\:)', re.MULTILINE)
    m = p.search(method.__doc__)
    return m.group(1)

def latex_doc(method):
    """
    returns rendered latex from doc string of method passed as parameter

    Format example for docstring:

            r\""" 
                    Foo Method Description 

                :latex: MULTI-LINE
                        LATEX EXPRESSION
                        INSERTED HERE

                :param bar: (example parameter)
                :returns: (whatever) 

                * [Notes] : 

                    - latex code must be followed by 
                        at least one ':'(like the one 
                        leading param above)

                    - doc string must be proceeded by r\""" 
            \"""

    :param: method with string literal doc string containing latex
    :returns: formated latex expression

    """  

    latex_string = extract_doc_latex(method)
    return display(Math(latex_string))

# example method with latex in doc string formated correctly
def foo(bar):
    r"""
            Example method with latex in doc string

        :latex: \text{Pythagorean Theorem} \\
                a^2 + b^2 = c^2
        :param bar: example parameter
        :returns: None
    """

# render doc string latex for example method above
latex_doc(foo)
