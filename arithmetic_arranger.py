"""
    Arithmetic Arranger
"""
import re


class BadInputError(Exception):
    """
        Exception raised for invalid input.

        Attributes:
            message -- explanation of the error
    """
    # No code needed here


def validate_problems(problems):
    """
        Validate problems function

        This function validates the input problems and raises a BadInputError if any of the following conditions are met:
        - There are more than 5 problems
        - Any of the operands is more than 4 digits long
        - Any of the operands contains non-digit characters
        - The operator is not '+' or '-'

        Parameters:
        problems (list): A list of strings representing arithmetic problems

        Returns:
        list: The input list of problems if they are valid

        Raises:
        BadInputError: If any of the input problems are invalid
    """
    allowed_operations = ['+', '-']
    if len(problems) > 5:
        raise BadInputError('Error: Too many problems.')
    for problem in problems:
        fragments = problem.split()
        (operand_a, operand_b) = (fragments[0], fragments[2])
        if len(operand_a) > 4 or len(operand_b) > 4:
            raise BadInputError(
                'Error: Numbers cannot be more than four digits.')
        try:
            int(operand_a)
            int(operand_b)
        except ValueError as exception:
            raise BadInputError(
                'Error: Numbers must only contain digits.') from exception
        operator = fragments[1]
        if operator not in allowed_operations:
            raise BadInputError("Error: Operator must be '+' or '-'.")

    return problems


def convert_to_tuple(valid_problems):
    """
        Convert valid problems to tuple

        This function takes a list of valid arithmetic problems and converts them into a list of tuples, where each tuple contains the first operand, the operator, and the second operand of each problem.

        Parameters:
        valid_problems (list): A list of valid arithmetic problems

        Returns:
        zip: A zip object containing tuples of the first operand, operator, and second operand of each problem
    """
    operand_a_list = []
    operator_list = []
    operand_b_list = []
    for problem in valid_problems:
        operand_a_list.append(re.search(r'\d+', problem).group())
        operator_list.append(re.search(r'\s([+-])\s', problem).group().strip())
        operand_b_list.append(re.search(r'\d+$', problem).group())

    return zip(operand_a_list, operator_list, operand_b_list)


def format_first_line(operand_a, box_width, problem_spacing):
    """
        Format first line

        This function formats the first line of an arithmetic problem.

        Parameters:
        operand_a (str): The first operand of the arithmetic problem
        box_width (int): The width of the box containing the arithmetic problem
        problem_spacing (str): The spacing between arithmetic problems

        Returns:
        str: The formatted first line of the arithmetic problem
    """
    prefix = ' '*(box_width - len(operand_a))
    prefix += problem_spacing
    return f'{prefix}{operand_a}'


def format_second_line(operator, operand_b, box_width, problem_spacing):
    """
        Format second line

        This function formats the second line of an arithmetic problem.

        Parameters:
        operator (str): The operator of the arithmetic problem
        operand_b (str): The second operand of the arithmetic problem
        box_width (int): The width of the box containing the arithmetic problem
        problem_spacing (str): The spacing between arithmetic problems

        Returns:
        str: The formatted second line of the arithmetic problem
    """
    prefix = ' '*(box_width - len(operand_b) - 1)
    return f'{problem_spacing}{operator}{prefix}{operand_b}'


def format_third_line(box_width, problem_spacing):
    """
        Format third line

        This function formats the third line of an arithmetic problem.

        Parameters:
        box_width (int): The width of the box containing the arithmetic problem
        problem_spacing (str): The spacing between arithmetic problems

        Returns:
        str: The formatted third line of the arithmetic problem
    """
    return f'{problem_spacing}{"-"*(box_width)}'


def calculate_solution(operand_a, operator, operand_b):
    """
        Calculate solution

        This function calculates the solution to an arithmetic problem.

        Parameters:
        operand_a (str): The first operand of the arithmetic problem
        operator (str): The operator of the arithmetic problem
        operand_b (str): The second operand of the arithmetic problem

        Returns:
        str: The solution to the arithmetic problem
    """
    solution = None
    if operator == '+':
        solution = int(operand_a) + int(operand_b)
    elif operator == '-':
        solution = int(operand_a) - int(operand_b)
    return str(solution)


def format_fourth_line(solution, box_width, problem_spacing):
    """
        Format fourth line

        This function formats the fourth line of an arithmetic problem.

        Parameters:
        solution (str): The solution to the arithmetic problem
        box_width (int): The width of the box containing the arithmetic problem
        problem_spacing (str): The spacing between arithmetic problems

        Returns:
        str: The formatted fourth line of the arithmetic problem
    """
    prefix = ' '*(box_width - len(solution))
    return f'{problem_spacing}{prefix}{solution}'


def arithmetic_arranger(problems, show_solution=False):
    """
        Arrange arithmetic problems vertically

        This function takes a list of arithmetic problems and arranges them vertically, 
            with each problem on a separate line. 
        The function also has an optional argument to show the solution to each problem.

        Parameters:
        problems (list): A list of arithmetic problems
        show_solution (bool): A boolean indicating whether to show the solution to each problem. 
            Default is False.

        Returns:
        str: A string containing the arranged arithmetic problems
    """
    try:
        valid_problems = validate_problems(problems)
    except BadInputError as error:
        return str(error)

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    for index, (operand_a, operator, operand_b) in enumerate(convert_to_tuple(valid_problems)):
        box_width = max(len(operand_a), len(operand_b)) + 2
        problem_spacing = ' '*4 if index > 0 else ''
        first_line += format_first_line(operand_a, box_width, problem_spacing)
        second_line += format_second_line(operator,
                                          operand_b, box_width, problem_spacing)
        third_line += format_third_line(box_width, problem_spacing)
        arranged_problems = f'{first_line}\n{second_line}\n{third_line}'
        if show_solution:
            fourth_line += format_fourth_line(
                calculate_solution(operand_a, operator, operand_b),
                box_width,
                problem_spacing)
            arranged_problems += f'\n{fourth_line}'

    return arranged_problems
