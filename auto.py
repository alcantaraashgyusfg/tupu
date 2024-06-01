def generate_html(file_list, starting_number):
    html_lines = []
    current_number = starting_number

    for file_name in file_list:
        html_line = f'<a href="soslal/agreg2/{file_name}">{current_number}</a>'
        html_lines.append(html_line)
        current_number += 1

    return html_lines

def main():
    file_name = input("Enter the name of the txt file containing file names: ")

    try:
        with open(file_name, 'r') as file:
            file_names = file.read().splitlines()
    except FileNotFoundError:
        print("File not found.")
        return

    starting_number = int(input("Enter the starting number: "))

    html_lines = generate_html(file_names, starting_number)

    output_file_name = "output_html.txt"

    with open(output_file_name, 'w') as output_file:
        output_file.write('\n'.join(html_lines))

    print(f"HTML lines generated and saved to {output_file_name}.")

if __name__ == "__main__":
    main()
