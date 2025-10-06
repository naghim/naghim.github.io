from enum import Enum
import tempfile
import subprocess
import multiprocessing
import copy
import sys
import os

### ENUMS ###
class InputType(Enum):
    FILE = 0
    CONSOLE = 1

class TestType(Enum):
    TEST_EQUAL = 0

class LanguageType(Enum):
    PYTHON = 0
    CPP = 1

### PROBLEMS ###

## Problem 1 ##
P1_CASE_1_INPUT = """q0 q1 q2
0 1
q0
q0
q0 0 q2
q0 1 q1
q1 0 q2
q1 1 q0
q2 0 q1
q2 1 q2"""

P1_CASE_1_OUTPUT = """IGEN
NEM
IGEN
IGEN
NEM"""

P1_CASE_2_INPUT = """q0 q1 q2
a b
q0
q1 q2
q0 a q1
q1 a q1
q1 b q2
q2 b q2"""

P1_CASE_2_OUTPUT = """IGEN
IGEN
NEM
NEM
IGEN
IGEN
NEM
NEM"""

## Problem 2 ##
P2_CASE_1_INPUT = """q0 q1 q2
0 1
q0
q2
q0 0 q1
q0 0 q2
q0 1 q1
q1 0 q2
q1 1 q2"""

P2_CASE_1_OUTPUT = """s0 s1 s2 s3
0 1
s0
s1 s3
s0 0 s1
s0 1 s2
s1 0 s3
s1 1 s3
s2 0 s3
s2 1 s3"""

P2_CASE_2_INPUT = """q0 q1 q2
0 1
q0
q2
q0 0 q0
q0 0 q1
q0 1 q0
q0 1 q1
q1 0 q1
q1 0 q2
q1 1 q0
q1 1 q1
q1 1 q2
q2 0 q1"""

P2_CASE_2_OUTPUT = """s0 s1 s2
0 1
s0
s2
s0 0 s1
s0 1 s1
s1 0 s2
s1 1 s2
s2 0 s2
s2 1 s2"""

P2_CASE_3_INPUT = """q0 q1 q2 q3
0 1
q0
q1 q3
q0 0 q2
q0 1 q1
q1 0 q1
q1 1 q2
q1 1 q3
q2 1 q2
q3 0 q2
q3 0 q3
q3 1 q2"""

P2_CASE_3_OUTPUT = """s0 s1 s2 s3
0 1
s0
s2 s3
s0 0 s1
s0 1 s2
s1 1 s1
s2 0 s2
s2 1 s3
s3 0 s3
s3 1 s1"""

P2_CASE_4_INPUT = """q0 q1
0 1
q0
q1
q0 0 q0
q0 1 q1
q1 0 q0
q1 1 q1"""

P2_CASE_4_OUTPUT = """s0 s1
0 1
s0
s1
s0 0 s0
s0 1 s1
s1 0 s0
s1 1 s1"""

P3_CASE_1_INPUT = """q0 q1 q2 q3 q4 q5
0 1
q0
q2
q0 0 q1
q0 1 q4
q1 0 q4
q1 1 q2
q2 0 q0
q2 1 q2
q3 0 q5
q3 1 q4
q4 0 q4
q4 1 q3
q5 0 q4
q5 1 q2"""

P3_CASE_1_OUTPUT_1 = """s0 s1 s2 s4
0 1
s0
s2
s0 0 s1
s0 1 s4
s1 0 s4
s1 1 s2
s2 0 s0
s2 1 s2
s4 0 s4
s4 1 s0"""

P3_CASE_1_OUTPUT_2 = """s0 s1 s2 s3
0 1
s0
s2
s0 0 s1
s0 1 s3
s1 0 s3
s1 1 s2
s2 0 s0
s2 1 s2
s3 0 s3
s3 1 s0"""

P3_CASE_2_INPUT = """q0 q1 q2 q3
0 1
q0
q2
q0 0 q1
q0 1 q3
q1 0 q3
q1 1 q2
q2 0 q0
q2 1 q2
q3 0 q3
q3 1 q0"""

P3_CASE_2_OUTPUT = """s0 s1 s2 s3
0 1
s0
s2
s0 0 s1
s0 1 s3
s1 0 s3
s1 1 s2
s2 0 s0
s2 1 s2
s3 0 s3
s3 1 s0"""

P3_CASE_3_INPUT = """q0 q1 q2
0 1
q0
q0 q2
q0 0 q1
q0 1 q2
q1 0 q1
q1 1 q2
q2 0 q1
q2 1 q2"""

P3_CASE_3_OUTPUT = """s0 s1
0 1
s0
s0
s0 0 s1
s0 1 s0
s1 0 s1
s1 1 s0"""

P4_CASE_1_INPUT = """q0 q1 q2
a b
z0 z1
q0
z0
q0
q0 a z0 z0z1 q1
q1 a z1 z1z1 q1
q1 b z1 E q2
q2 b z1 E q2
q2 E z0 E q0"""

P4_CASE_1_OUTPUT = """IGEN
NEM
NEM
NEM
NEM
NEM"""

P4_CASE_2_INPUT = """q0 q1 q2 q3
a b
z0 z1
q0
z0
q3
q0 a z0 z0z1 q1
q1 a z1 z1z1 q1
q1 b z1 E q2
q2 b z1 E q2
q2 b z0 z0z0 q2
q2 E z0 E q0"""

P4_CASE_2_OUTPUT = """IGEN
IGEN
NEM
NEM
NEM"""

problems = [
    {
        'name': 'Problem 1 (DFA - Deterministic Finite Automaton)',
        'enabled': True,
        'cases': [
            {
                'name': 'Case 1',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P1_CASE_1_INPUT,
                'output': P1_CASE_1_OUTPUT,
                'arguments': ['--check', '10101,111,111110111010101,001,0021']
            },
            {
                'name': 'Case 2',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P1_CASE_2_INPUT,
                'output': P1_CASE_2_OUTPUT,
                'arguments': ['--check', 'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']
            }
        ]
    },
    {
        'name': 'Problem 2 (Transforming a Non-Deterministic Finite Automata Into a Deterministic One)',
        'enabled': True,
        'cases': [
            {
                'name': 'Case 1',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P2_CASE_1_INPUT,
                'output': P2_CASE_1_OUTPUT,
                'arguments': ['--det']
            },
            {
                'name': 'Case 2',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P2_CASE_2_INPUT,
                'output': P2_CASE_2_OUTPUT,
                'arguments': ['--det']
            },
            {
                'name': 'Case 3',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P2_CASE_3_INPUT,
                'output': P2_CASE_3_OUTPUT,
                'arguments': ['--det']
            },
            {
                'name': 'Case 4',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P2_CASE_4_INPUT,
                'output': P2_CASE_4_OUTPUT,
                'arguments': ['--det']
            }
        ]
    },
    {
        'name': 'Problem 3 (Minimizing a Finite Automaton)',
        'enabled': False,
        'cases': [
            {
                'name': 'Case 1',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P3_CASE_1_INPUT,
                'output': [P3_CASE_1_OUTPUT_1, P3_CASE_1_OUTPUT_2],
                'arguments': ['--mini']
            },
            {
                'name': 'Case 2',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P3_CASE_2_INPUT,
                'output': P3_CASE_2_OUTPUT,
                'arguments': ['--mini']
            },
            {
                'name': 'Case 3',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P3_CASE_3_INPUT,
                'output': P3_CASE_3_OUTPUT,
                'arguments': ['--mini']
            }
        ]
    },
    {
        'name': 'Problem 4 (Stack Automaton)',
        'enabled': False,
        'cases': [
            {
                'name': 'Case 1',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P4_CASE_1_INPUT,
                'output': P4_CASE_1_OUTPUT,
                'arguments': ['--stack', 'aabb,abb,aab,abab,a,b']
            },
            {
                'name': 'Case 2',
                'inputType': InputType.FILE,
                'testType': TestType.TEST_EQUAL,
                'input': P4_CASE_2_INPUT,
                'output': P4_CASE_2_OUTPUT,
                'arguments': ['--stack', 'ab,abb,aaabb,a,b']
            }
        ]
    }
]

class AutograderException(Exception):
    pass

def get_random_filename():
    return os.path.join(tempfile._get_default_tempdir(), next(tempfile._get_candidate_names()))

def create_arguments(environment, case):
    command = copy.deepcopy(environment['languageCommand'])
    arguments = case.get('arguments', [])

    # Pass input and output filename to the program
    if case['inputType'] == InputType.FILE:
        command.extend(['--input', environment['input'], '--output', environment['output']])    

    # Pass stdin to the program
    if case['inputType'] == InputType.CONSOLE:
        stdin = case['input'] + '\n'
        encoding = 'utf-8'
    else:
        stdin = None
        encoding = None

    if arguments:
        command.extend(arguments)

    environment['command'] = command
    environment['stdin'] = stdin
    environment['encoding'] = encoding

def run_program(environment, case):
    create_arguments(environment, case)

    try:
        # We need the output, so capture_output=True, and we need the output as text, so text=True
        # We also need to check if the process was successful, so check=True
        process = subprocess.run(environment['command'], cwd=environment['cwd'], capture_output=True, text=True, input=environment['stdin'], encoding=environment['encoding'])

        for val in [process.stdout, process.stderr]:
            if val:
                val = val.strip()
                if val:
                    print(val.strip())

        if process.returncode != 0:
            raise AutograderException(f"Program exited with status code {process.returncode}")

        environment['stdout'] = process.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise AutograderException(f"Couldn't run project: {e}")

### LANGUAGE-SPECIFIC CODE ###
def find_python_package(folder: str) -> dict:
    for root, _, files in os.walk(folder):
        for file in files:
            if file == '__main__.py':
                root_folder = os.path.dirname(root)
                package = os.path.basename(root)
                return {'language': LanguageType.PYTHON, 'root': root_folder, 'package': package}

    return None

def find_cmake_folder(folder: str) -> dict:
    for root, _, files in os.walk(folder):
        for file in files:
            if file == 'CMakeLists.txt':
                return {'language': LanguageType.CPP, 'root': root}

    return None

def find_executable(folder: str) -> str:
    for root, _, files in os.walk(folder):
        for file in files:
            filename = os.path.join(root, file)

            try:
                with open(filename, 'rb') as f:
                    if f.read(4) == b'\x7fELF':
                        return filename
            except:
                # Could not read this file, forget about it
                pass

    return None

def prepare_python_code(environment):
    package_name = environment['package']
    environment['cwd'] = environment['root']
    environment['languageCommand'] = ['python3', '-m', package_name]

def prepare_cpp_code(environment):
    build_folder = tempfile.mkdtemp()

    try:
        subprocess.run(['cmake', '-DCMAKE_BUILD_TYPE=Release', environment['root']], cwd=build_folder, check=True)
    except subprocess.CalledProcessError as e:
        raise AutograderException(f'Could not configure CMake project')

    try:
        subprocess.run(['make', '-j', str(multiprocessing.cpu_count())], cwd=build_folder)
    except subprocess.CalledProcessError as e:
        raise AutograderException(f'Could not build CMake project')
    
    executable = find_executable(build_folder)

    if not executable:
        raise AutograderException(f"Couldn't find built executable in CMake project")

    environment['cwd'] = build_folder
    environment['languageCommand'] = [executable]

### INPUT-SPECIFIC CODE ###
def setup_input_file(case, environment):
    input_file = get_random_filename()
    output_file = get_random_filename()

    environment['input'] = input_file
    environment['output'] = output_file

    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(case['input'])

def verify_input_file(case, environment):
    input_file = environment['input']
    output_file = environment['output']

    if not os.path.exists(output_file):
        raise AutograderException(f"Output file not created by program")

    with open(output_file, 'r', encoding='utf-8') as f:
        output = f.read().strip()

    if not tests[case['testType']](case, output):
        raise AutograderException(f"Output mismatch: expected different output in file")

    if os.path.exists(input_file):
        os.remove(input_file)

    if os.path.exists(output_file):
        os.remove(output_file)

def verify_stdout(case, environment):
    if not tests[case['testType']](case, environment['stdout']):
        raise AutograderException(f"Output mismatch: expected different output on stdout")

### TEST-SPECIFIC CODE###
def strip_lines(text):
    return '\n'.join([line.strip() for line in text.strip().split('\n')])

def test_equal(case, output):
    actual_output = strip_lines(output)
    expected_output = case['output']
    expected_outputs = [expected_output] if isinstance(expected_output, str) else expected_output

    return any([strip_lines(o) == actual_output for o in expected_outputs])

### MAIN CODE ###
languages = {
    LanguageType.PYTHON: {
        'name': 'Python',
        'find': find_python_package,
        'prepare': prepare_python_code,
    },
    LanguageType.CPP: {
        'name': 'CMake (C++)',
        'find': find_cmake_folder,
        'prepare': prepare_cpp_code
    }
}

inputs = {
    InputType.FILE: {
        'setup': setup_input_file,
        'verify': verify_input_file
    },
    InputType.CONSOLE: {
        'setup': None,
        'verify': verify_stdout
    }
}

tests = {
    TestType.TEST_EQUAL: test_equal
}

def run_all_cases():
    folder = os.getcwd()
    environment = None

    for language, language_info in languages.items():
        environment = language_info['find'](folder)

        if environment:
            break

    if not environment:
        print("❌ Couldn't find any project in the current folder ❌")
        sys.exit(1)

    print(f"Found {language_info['name']} project in {environment['root']}")

    try:
        language_info['prepare'](environment)
    except AutograderException as e:
        print(f"❌ Error during build: {e}")
        sys.exit(2)

    print("Running tests...")
    failed = False

    for problem in problems:
        if not problem['enabled']:
            continue

        print(f"Problem: {problem['name']}")

        for case in problem['cases']:
            print(f"Running case: {case['name']}")

            try:
                input_type = inputs[case['inputType']]
                
                if input_type['setup']:
                    input_type['setup'](case, environment)

                run_program(environment, case)

                if case['inputType']:
                    input_type['verify'](case, environment)
            except AutograderException as e:
                print(f"❌ Failed {case['name']}: {e} ❌")
                failed = True
                continue

            print(f"🎉 {case['name']} succeeded 🎉")
    
    if failed:
        print("❌ Some tests failed. ❌")
        sys.exit(3)

    print("🎉 All tests passed! Congratulations! 🎉")
    sys.exit(0)

if __name__ == "__main__":
    run_all_cases()
