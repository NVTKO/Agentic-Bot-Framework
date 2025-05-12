def get_tools():
    return {
        "math": lambda x: eval(x),                        # Simple calculator
        "file_read": lambda path: open(path, 'r').read()  # Read file content
    }