from binarytree2050 import BinaryTree
from stack2050 import Stack
import operator
import unittest


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:

        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i.isnumeric():
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent

        elif i == ')':
            currentTree = pStack.pop()

        else:
            print("token '{}' is not a valid integer".format(i))
            return None

    return eTree


def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()


def printExpression(tree):
    sVal = ""
    if tree:
        sVal = '( ' + printExpression(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal()) + ' '
        sVal = sVal + printExpression(tree.getRightChild()) + ') '
    return sVal


class TestParseTreeFunctions(unittest.TestCase):

    def testEval(self):
        input_str = "( ( 3 + 7 ) * ( 4 + 5 ) )"
        pt = buildParseTree(input_str)
        result = evaluate(pt)
        self.assertEqual(result, 90)


def main():
    input_str = "( ( 3 + 7 ) * ( 4 + 5 ) )"
    pt = buildParseTree(input_str)
    #print("Evaluating parse tree... \n  result = ", evaluate(pt))
    print(printExpression(pt))
    print(" preOrder traversal: \n")
    pt.preOrder()
    print(" inOrder traversal: \n")
    pt.inOrder()
    print(" postOrder traversal: \n")
    pt.postOrder()

# unittest_main() - run unittest's main, which runs TestParseTreeFunctions's methods
def unittest_main():
    print("-"*25, "running unit tests", "-"*25)
    unittest.main()

# evaluates to true if run as standalone program (e.g. $ python parsetree.py)
if __name__ == '__main__':
    main()
    #unittest_main()
