"""
The story
"""
story: dict = {
    'point1': { 
        'Q': 'Where do you want to go?',
        'A': {'Left': 'point2', 'Right': 'point3'}
        },
    'point2': { 
        'Q': 'Where do you want to go?',
        'A': {'Left': 'point1', 'Right': 'point3'}
        },
    'point3': { 
        'Q': 'Where do you want to go?',
        'A': {'Left': 'point2', 'Middle': 'point4', 'Right': 'point4', 'Exit': 'exit'}
        },
    'point4': { 
        'Q': 'Where do you want to go?',
        'A': {'Left': 'point3', 'Right': 'point1', 'Middle': 'point2'}
        }
}
