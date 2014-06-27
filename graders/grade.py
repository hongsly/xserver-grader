def grade(grader_path, grader_config, student_response, sandbox):
    print grader_path, grader_config, student_response, sandbox

    sandbox_cmd = ' '.join(sandbox.sandbox_cmd_list())
    
    results = {
        'correct': False,
        'score': 1,
        'tests': [
	('short description 1','long description 1',False,'expected1','actual1'),
	('short 2', 'sandbox_cmd: '+sandbox_cmd,False,'grader_path: '+str(grader_path), 'student_response: '+student_response),
	('short 3','grader_config: '+str(grader_config), True, 'e3',str(eval('2+3'))),
	],
        'errors': []
    }
    return results
