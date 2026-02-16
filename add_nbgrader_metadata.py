import json
import sys

def add_nbgrader_metadata(notebook_path):
    """Add NBGrader metadata to cells containing solution/test markers"""
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    assignment_points = {
        'A1': 10,
        'A2': 15,
        'A3': 10,
        'A4': 15,
        'A5': 15,
        'A6': 25
    }
    
    current_exercise = None
    solution_counter = 0
    
    for cell in notebook['cells']:
        source = ''.join(cell['source'])
        
        # Check if this is an exercise header
        for ex_id in assignment_points:
            if f'Exercise {ex_id}' in source:  # Match both "## Exercise A1" and "**Exercise A1"
                current_exercise = ex_id
                print(f"Found exercise header: {ex_id}")
                break
        
        # Initialize metadata if needed
        if 'metadata' not in cell:
            cell['metadata'] = {}
        
        # Add nbgrader metadata for solution cells
        if '### BEGIN SOLUTION' in source and '### END SOLUTION' in source:
            solution_counter += 1
            grade_id = f'{current_exercise}_solution' if current_exercise else f'solution_{solution_counter}'
            cell['metadata']['nbgrader'] = {
                'grade': False,
                'grade_id': grade_id,
                'locked': False,
                'schema_version': 3,
                'solution': True,
                'task': False
            }
            print(f"Added solution metadata: {grade_id}")
        
        # Add nbgrader metadata for test cells
        elif '### BEGIN HIDDEN TESTS' in source and '### END HIDDEN TESTS' in source:
            if current_exercise:
                cell['metadata']['nbgrader'] = {
                    'grade': True,
                    'grade_id': f'{current_exercise}_tests',
                    'locked': True,
                    'points': assignment_points.get(current_exercise, 0),
                    'schema_version': 3,
                    'solution': False,
                    'task': False
                }
                print(f"Added test metadata: {current_exercise}_tests ({assignment_points.get(current_exercise, 0)} points)")
    
    # Save the modified notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print(f"\nSuccessfully updated {notebook_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python add_nbgrader_metadata.py <notebook_path>")
        sys.exit(1)
    
    add_nbgrader_metadata(sys.argv[1])
