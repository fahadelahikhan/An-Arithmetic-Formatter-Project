def arithmetic_arranger(problems, show_answers=False):
    # Check for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists to hold each line of the formatted problems
    top_lines = []
    bottom_lines = []
    dash_lines = []
    answer_lines = []

    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        operand1, operator, operand2 = parts

        # Check for valid operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check that operands are digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check operand lengths
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the maximum width of the operands
        max_width = max(len(operand1), len(operand2)) + 2

        # Format the top, bottom, and dash lines
        top = operand1.rjust(max_width)
        bottom = operator + ' ' + operand2.rjust(max_width - 2)
        dash = '-' * max_width

        top_lines.append(top)
        bottom_lines.append(bottom)
        dash_lines.append(dash)

        # Calculate the answer if required
        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answer = answer.rjust(max_width)
            answer_lines.append(answer)

    # Combine all lines into the final formatted string
    arranged_problems = '    '.join(top_lines) + '\n'
    arranged_problems += '    '.join(bottom_lines) + '\n'
    arranged_problems += '    '.join(dash_lines)

    # Add answers if required
    if show_answers:
        arranged_problems += '\n' + '    '.join(answer_lines)

    return arranged_problems
