from binarytree2050 import BinaryTree
from parsetree import printExpression  # binarytree2050.py from MS Teams
from stack2050 import Stack            # stacks2050.py from MS Teams
import operator
import unittest
import random

"""
------------------------------ REFERENCE LIST DELETE LATER ------------------------------------------------

    T - denotes True
    F - denotes False
    U_x is an 'unlikely' symbol that evaluates to True with probability x, 0.0 <= x < 0.5
    L_x is a 'likely' symbol that evaluates to True w/ probability x, 0.5 <= x < 1.0
    AND, OR - the two operators (note, these are binary operators)
    (, ) - parentheses are to be used in the same way as with the parsetree.py example we saw in class

====== Some additional examples of statements in this language are: ======================================

    ( T AND F ) a should evaluate to False
    ( T OR F ) a should evaluate to True
     L_0.7  a should evaluate to True 70% of the time
     U_0.9  invalid since parameter x is greater than 0.5
    ( ( L_0.8 AND T  ) OR  U_0.25  ) should evaluate to True 85% of the time

------------------------------------------------------------------------------------------------------------
"""


# IN ADDITION TO IMPLEMENTING THE FUNCTIONS BELOW, BE SURE THAT YOU ALSO
# DOCUMENT ALL OF YOUR CODE, AND ANY AUXILIARY FUNCTIONS YOU CREATE
# (AND BE SURE TO REPLACE/REMOVE THESE PLACEHOLDER COMMENTS IN ALL CAPS)

def buildParseTree(prob_logic_expression):
    """
    INSERT YOUR DOCUMENTATION HERE (REMOVE COMMENTS IN ALL CAPS)
    """
    token_list = prob_logic_expression.split()
    my_stack = Stack()
    probLogicTree = BinaryTree('')
    my_stack.push(probLogicTree)
    currentTree = probLogicTree

    for tok in token_list:
        if tok == '(':
            currentTree.insertLeft('')
            my_stack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif tok in ['AND', 'OR']:
            currentTree.setRootVal(tok)
            currentTree.insertRight('')
            my_stack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif tok[0] in ['T', 'F', 'U', 'L']:
            currentTree.setRootVal(tok)
            parent = my_stack.pop()
            currentTree = parent

        elif tok == ')':
            currentTree = my_stack.pop()

    return probLogicTree


def evaluateParseTree(parse_tree):
    """
    INSERT YOUR DOCUMENTATION HERE (REMOVE COMMENTS IN ALL CAPS)
    """
    tokens = {'AND':operator.and_(), 'OR':operator.or_(), 'T':True, 'F':False}

    leftC = parse_tree.getLeftChild()
    rightC = parse_tree.getRightChild()

    if leftC and rightC:
        fn = tokens[parse_tree.getRootVal()]
        return fn(evaluateParseTree(leftC),evaluateParseTree(rightC))
    else: 
        return parse_tree.getRootVal()


def printParseTree(parse_tree):
    """
    INSERT YOUR DOCUMENTATION HERE (REMOVE COMMENTS IN ALL CAPS)
    """
    retVal = ""
    if parse_tree:
        retVal = '(' + printParseTree(parse_tree.getLeftChild())
        retVal = retVal + str(parse_tree.getRootVal()) + ' '
        retVal = retVal + printExpression(parse_tree.getRightChild()) + ')'
    return retVal



class TestProbLogicTreeFunctions(unittest.TestCase):

    def testA(self):
        ...

    def testB(self):
        ...

    """
    MUST HAVE AT LEAST TWO TESTS (REMOVE COMMENTS IN ALL CAPS)
    """


def main():
    random.seed(1)
    expression = "( ( T AND L_0.5 ) OR ( L_0.8 OR F ) )"
    #expression = "( T AND F )"
    pt = buildParseTree(expression)
    #print("Evaluating parse tree one time...", evaluateParseTree(pt))

    # l = [evaluateParseTree(pt) for i in range(5000)]
    # print(f"Avg proportion of time tree evaluates to True: {sum(l)/len(l):.4f}")

    exp_tmp = printParseTree(pt)
    exp = exp_tmp.replace(' ', '')
    print("Printed parse tree:", exp)

# unittest_main() - run unittest's main to run test methods in TestProbLogicTreeFunctions
def unittest_main():
    print("-"*25, "running unit tests", "-"*25)
    unittest.main()

# evaluates to true if run as standalone program (e.g. $ python assign5.py)
if __name__ == '__main__':
    main()
    unittest_main()
