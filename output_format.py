"""
This variable can be changed to adjust the data that's included in the output.
"""

output_format = {
    'poseKeyframes': {
        'Name': 'Position',
        'fields': [
            'Time',
            'Head.Position.X',
            'Head.Position.Y',
            'Head.Position.Z',
            'Head.Rotation.X',
            'Head.Rotation.Y',
            'Head.Rotation.Z',
            'Head.Rotation.W',
            'Left.Position.X',
            'Left.Position.Y',
            'Left.Position.Z',
            'Left.Rotation.X',
            'Left.Rotation.Y',
            'Left.Rotation.Z',
            'Left.Rotation.W',
            'Right.Position.X',
            'Right.Position.Y',
            'Right.Position.Z',
            'Right.Rotation.X',
            'Right.Rotation.Y',
            'Right.Rotation.Z',
            'Right.Rotation.W',
        ],
    },
    'noteKeyframes': {
        'Name': 'Notes',
        'fields': [
             'Time',
             'NoteID',
             'EventType',
             'BeforeCutRating',
             'AfterCutRating',
        ]
    },
}
