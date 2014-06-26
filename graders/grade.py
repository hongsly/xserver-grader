def grade(grader_path, grader_config, student_response, sandbox):
    print grader_path, grader_config, student_response, sandbox
    
    results = {
        'correct': False,
        'score': 1,
        'tests': [('a','b','c','d','e')],
        'errors': []
    }
    return results
