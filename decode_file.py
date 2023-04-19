from decode_utils import *

from lzma import decompress as lzma_decompress


def deserialize(input_bytes):
    pointers = read_pointers(input_bytes, { 'offset': 0 })

    replay_file = {
        'metadata': read_metadata(input_bytes, { 'offset': pointers.metadata }),
        'poseKeyframes': read_pose_group_list(input_bytes, { 'offset': pointers.poseKeyframes }),
        'heightKeyframes': read_height_change_list(input_bytes, { 'offset': pointers.heightKeyframes }),
        'noteKeyframes': read_note_event_list(input_bytes, { 'offset': pointers.noteKeyframes }),
        'scoreKeyframes': read_score_event_list(input_bytes, { 'offset': pointers.scoreKeyframes }),
        'comboKeyframes': read_combo_event_list(input_bytes, { 'offset': pointers.comboKeyframes }),
        'multiplierKeyframes': read_multiplier_event_list(input_bytes, { 'offset': pointers.multiplierKeyframes }),
        'energyKeyframes': read_energy_event_list(input_bytes, { 'offset': pointers.energyKeyframes })
    }

    return replay_file


def decompress(filename):
    with open(filename, 'rb') as f:
        serialized_data = f.read()

    serialized_data = bytearray(serialized_data[28:])
    return lzma_decompress(serialized_data)
