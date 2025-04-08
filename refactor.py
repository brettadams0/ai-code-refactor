import ast
import random
import re
import time
import copy
from collections import Counter

# Simulated "AI model" for refactoring (small decision tree or heuristic-based model)
class CodeRefactorAI:
    def __init__(self):
        self.refactor_rules = [
            ("Use list comprehensions", self.is_for_loop),
            ("Simplify nested ifs", self.is_nested_if),
            ("Replace recursion with iteration", self.is_recursion),
            ("Remove unnecessary variables", self.is_unnecessary_var)
        ]
    
    def suggest_refactor(self, code_ast):
        suggestions = []
        for rule_name, rule_func in self.refactor_rules:
            if rule_func(code_ast):
                suggestions.append(rule_name)
        return suggestions

    def is_for_loop(self, code_ast):
        """Detects if there is an inefficient for loop"""
        for node in ast.walk(code_ast):
            if isinstance(node, ast.For) and isinstance(node.target, ast.Name):
                # Example: Replace 'for i in range(len(x))' with 'for x_item in x'
                if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name):
                    return True
        return False

    def is_nested_if(self, code_ast):
        """Detects nested if statements that can be simplified"""
        for node in ast.walk(code_ast):
            if isinstance(node, ast.If) and isinstance(node.test, ast.BoolOp):
                return True
        return False

    def is_recursion(self, code_ast):
        """Detects recursive functions"""
        functions = [node for node in ast.walk(code_ast) if isinstance(node, ast.FunctionDef)]
        for func in functions:
            for node in ast.walk(func):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == func.name:
                    return True
        return False

    def is_unnecessary_var(self, code_ast):
        """Detects unnecessary variables"""
        variable_usages = Counter()
        for node in ast.walk(code_ast):
            if isinstance(node, ast.Name):
                variable_usages[node.id] += 1
        return any(count > 1 for count in variable_usages.values())

    def refactor_code(self, code_ast):
        """Perform actual refactoring based on the model's suggestions."""
        refactored_code = copy.deepcopy(code_ast)
        for node in ast.walk(refactored_code):
            if isinstance(node, ast.For):
                # Simplify for loop if necessary
                if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name):
                    node.target.id = "x_item"  # Just an example refactor
        return refactored_code

class CodeOptimizer:
    def __init__(self):
        pass

    def optimize(self, code_ast):
        """Optimize code for performance. For example, remove redundant code."""
        for node in ast.walk(code_ast):
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.Add):
                    # Simplify redundant expressions like 'a = a + 1'
                    if isinstance(node.value.left, ast.Name) and isinstance(node.value.right, ast.Constant):
                        node.value = node.value.left  # Optimizing this redundant add operation
        return code_ast

    def generate_code_quality_score(self, code_ast):
        """Generate a score based on complexity (for simplicity, we use line count)."""
        num_lines = sum(1 for _ in ast.walk(code_ast))
        return 100 - (num_lines // 10)  # Simple score based on line count

def analyze_and_refactor_code(code):
    # Parse the code into an AST (Abstract Syntax Tree)
    tree = ast.parse(code)

    # Create instances of AI-based refactorer and optimizer
    refactor_ai = CodeRefactorAI()
    optimizer = CodeOptimizer()

    # AI suggestions
    suggestions = refactor_ai.suggest_refactor(tree)
    if suggestions:
        print("Suggestions for refactoring:")
        for suggestion in suggestions:
            print(f"  - {suggestion}")
    
    # Refactor code (e.g., optimize for loops, etc.)
    refactored_tree = refactor_ai.refactor_code(tree)
    
    # Optimize code for performance (remove redundancies, etc.)
    optimized_tree = optimizer.optimize(refactored_tree)

    # Generate quality score
    score = optimizer.generate_code_quality_score(optimized_tree)
    print(f"Code Quality Score: {score}/100")

    # Convert AST back to code (using astor or similar method in real implementation)
    refactored_code = ast.unparse(optimized_tree)  # Python 3.9+ feature

    return refactored_code

# Example Usage:
example_code = """
def example(a, b):
    x = a + b
    for i in range(len(x)):
        print(i)
    return x
"""

print("Original Code:")
print(example_code)

refactored_code = analyze_and_refactor_code(example_code)

print("\nRefactored Code:")
print(refactored_code)
