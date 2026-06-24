def arithmetic_arranger(problems, show_answers=False):
    # Rule 1: Check for too many problems (Limit is 5)
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        # Split the string components into operand1, operator, operand2
        parts = problem.split()
        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        # Rule 2: Verify allowed operators (+ or - only)
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Rule 3: Ensure numbers contain only valid digits
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        # Rule 4: Max width limit of four digits per number
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate exact visual spacing length required for this specific problem block
        longest_operand = max(len(num1), len(num2))
        total_width = longest_operand + 2

        # Format rows using right-alignment padding structures
        top_row = num1.rjust(total_width)
        bottom_row = operator + num2.rjust(total_width - 1)
        dashes = '-' * total_width

        first_line.append(top_row)
        second_line.append(bottom_row)
        dash_line.append(dashes)

        # Process mathematical answers if flag parameter is explicitly declared True
        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answer_row = result.rjust(total_width)
            answer_line.append(answer_row)

    # Join problem blocks together with exactly 4 spacing segments between columns
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dash_line)
    )

    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_line)

    return arranged_problems
