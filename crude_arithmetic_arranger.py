"""
    Arithmetic Arranger
"""

def arithmetic_arranger(problems, show_solution=False):
    """
        Arithmetic Arranger Function
    """
    # crude solution
    arranged_problems = ''
    for problem in problems:
        fragments = problem.split()
        first_num__str = fragments[0]
        operator__str = fragments[1]
        second_num__str = fragments[2]
        box_width = max(len(fragments[0]), len(fragments[2])) + 2
        first_line = f'{" "*(box_width - len(first_num__str) - 1)} {first_num__str}'
        second_line = f'{operator__str}{" "*(box_width - len(second_num__str) - 1)}{second_num__str}'
        third_line = f'{"_"*box_width}'
        arranged_problem = f'{first_line}\n{second_line}\n{third_line}'
        if show_solution:
            solution = None
            if operator__str == '+':
                solution = int(first_num__str) + int(second_num__str)
            elif operator__str == '-':
                solution = int(first_num__str) - int(second_num__str)

            fourth_line = f'{" "*(box_width - len(str(solution)))}{solution}'
            arranged_problem += f'\n{fourth_line}'
        arranged_problems += arranged_problem + '\n'
