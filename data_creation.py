import subprocess

def process_csv_with_machine_reading(input_csv, output_file=None, delimiter=',', namespace='https://w3id.org/stlab/mr_data/', mode='all'):
    
    script_path = "C:/Users/casaz/machine-reading/mr.py"
    working_directory = "C:/Users/casaz/machine-reading"
    
    # Base command
    command = ["python", script_path, input_csv]

    # Add optional arguments
    if output_file:
        command.extend(["-o", output_file])
    if delimiter:
        command.extend(["-d", delimiter])
    if namespace:
        command.extend(["-n", namespace])
    if mode:
        command.extend(["-m", mode])

    # Execute the command
    try:
        result = subprocess.run(command, cwd=working_directory, check=True, text=True, capture_output=True)
        print("Output:", result.stdout)
        print("Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e.stderr)

# Example usage
if __name__ == "__main__":
    # Input and output file paths
    input_csv = "C:/Users/casaz/Documents/Simone/University/dhdk/krae/alien_project/alien_repository/E.T-and-visual-culture-ontology-perspectives-on-Extraterrestrial-influence-in-visual-heritage-ETVCO-/data/test_data.csv"
    output_file = "C:/Users/casaz/Documents/Simone/University/dhdk/krae/alien_project/alien_repository/E.T-and-visual-culture-ontology-perspectives-on-Extraterrestrial-influence-in-visual-heritage-ETVCO-/data/output.nq"

    # Call the function
    process_csv_with_machine_reading(
        input_csv=input_csv,
        output_file=output_file,
        delimiter=',',
        namespace='https://example.org/custom_namespace/',
        mode='all'  # Options: 'fred', 'amr2fred', 'all'
    )
