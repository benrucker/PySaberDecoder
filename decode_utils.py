import struct

from structs import ComboEvent, EnergyEvent, HeightEvent, Metadata, MultiplierEvent, NoteEvent, NoteEventType, NoteID, Pointers, ScoreEvent, VRPose, VRPoseGroup, VRPosition, VRRotation


# Primitives
def read_string(input: bytes, offset: dict[int]) -> str:
    string_length = struct.unpack_from("<i", input, offset['offset'])[0]
    value = input[offset['offset'] + 4: offset['offset'] + 4 + string_length].decode("utf-8")
    offset['offset'] += string_length + 4
    return value


def read_int(input: bytes, offset: dict[int]) -> int:
    value = struct.unpack_from("<i", input, offset['offset'])[0]
    offset['offset'] += 4
    return value


def read_float(input: bytes, offset: dict[int]) -> float:
    value = struct.unpack_from("<f", input, offset['offset'])[0]
    offset['offset'] += 4
    return value


def read_bool(input: bytes, offset: dict[int]) -> bool:
    value = struct.unpack_from("<?", input, offset['offset'])[0]
    offset['offset'] += 1
    return value


# Not primitives
def read_vr_position(input: bytes, offset: dict[int]):
    return VRPosition(
        read_float(input, offset),
        read_float(input, offset),
        read_float(input, offset)
    )


def read_vr_rotation(input: bytes, offset: dict[int]):
    return VRRotation(
        read_float(input, offset),
        read_float(input, offset),
        read_float(input, offset),
        read_float(input, offset)
    )


# Lists
def read_string_array(_input: bytes, offset: dict[int]) -> list[str]:
    size = read_int(_input, offset)
    values = [read_string(_input, offset) for _ in range(size)]
    return values


def read_pose_group_list(_input: bytes, offset: dict[int]) -> list[VRPoseGroup]:
    size = read_int(_input, offset)
    values = [read_vr_pose_group(_input, offset) for _ in range(size)]
    return values


def read_height_change_list(_input: bytes, offset: dict[int]) -> list[HeightEvent]:
    size = read_int(_input, offset)
    values = [read_height_change(_input, offset) for _ in range(size)]
    return values


def read_note_event_list(_input: bytes, offset: dict[int]) -> list[NoteEvent]:
    size = read_int(_input, offset)
    values = [read_note_event(_input, offset) for _ in range(size)]
    return values


def read_score_event_list(_input: bytes, offset: dict[int]) -> list[ScoreEvent]:
    size = read_int(_input, offset)
    values = [read_score_event(_input, offset) for _ in range(size)]
    return values


def read_combo_event_list(_input: bytes, offset: dict[int]) -> list[ComboEvent]:
    size = read_int(_input, offset)
    values = [read_combo_event(_input, offset) for _ in range(size)]
    return values


def read_multiplier_event_list(_input: bytes, offset: dict[int]) -> list[MultiplierEvent]:
    size = read_int(_input, offset)
    values = [read_multiplier_event(_input, offset) for _ in range(size)]
    return values


def read_energy_event_list(_input: bytes, offset: dict[int]) -> list[EnergyEvent]:
    size = read_int(_input, offset)
    values = [read_energy_event(_input, offset) for _ in range(size)]
    return values


# Structs
def read_pointers(input, offset):
    return Pointers(metadata=read_int(input, offset),
                    poseKeyframes=read_int(input, offset),
                    heightKeyframes=read_int(input, offset),
                    noteKeyframes=read_int(input, offset),
                    scoreKeyframes=read_int(input, offset),
                    comboKeyframes=read_int(input, offset),
                    multiplierKeyframes=read_int(input, offset),
                    energyKeyframes=read_int(input, offset),
                    fpsKeyframes=read_int(input, offset))


def read_metadata(input, offset):
    return Metadata(Version=read_string(input, offset),
                    LevelID=read_string(input, offset),
                    Difficulty=read_int(input, offset),
                    Characteristic=read_string(input, offset),
                    Environment=read_string(input, offset),
                    Modifiers=read_string_array(input, offset),
                    NoteSpawnOffset=read_float(input, offset),
                    LeftHanded=read_bool(input, offset),
                    InitialHeight=read_float(input, offset),
                    RoomRotation=read_float(input, offset),
                    RoomCenter=read_vr_position(input, offset),
                    FailTime=read_float(input, offset))


def read_vr_pose_group(input, offset):
    return VRPoseGroup(Head=read_vr_pose(input, offset),
                       Left=read_vr_pose(input, offset),
                       Right=read_vr_pose(input, offset),
                       FPS=read_int(input, offset),
                       Time=read_float(input, offset))


def read_vr_pose(input, offset):
    return VRPose(Position=read_vr_position(input, offset),
                  Rotation=read_vr_rotation(input, offset))


def read_note_event(input, offset):
    return NoteEvent(NoteID=read_note_id(input, offset),
                     EventType=NoteEventType(read_int(input, offset)),
                     CutPoint=read_vr_position(input, offset),
                     CutNormal=read_vr_position(input, offset),
                     SaberDirection=read_vr_position(input, offset),
                     SaberType=read_int(input, offset),
                     DirectionOK=read_bool(input, offset),
                     SaberSpeed=read_float(input, offset),
                     CutAngle=read_float(input, offset),
                     CutDistanceToCenter=read_float(input, offset),
                     CutDirectionDeviation=read_float(input, offset),
                     BeforeCutRating=read_float(input, offset),
                     AfterCutRating=read_float(input, offset),
                     Time=read_float(input, offset),
                     UnityTimescale=read_float(input, offset),
                     TimeSyncTimescale=read_float(input, offset),
                     # New in V3
                     TimeDeviation=read_float(input, offset),
                     WorldRotation=read_vr_rotation(input, offset),
                     InverseWorldRotation=read_vr_rotation(input, offset),
                     NoteRotation=read_vr_rotation(input, offset),
                     NotePosition=read_vr_position(input, offset)
                     )


def read_note_id(input, offset):
    return NoteID(Time=read_float(input, offset),
                  LineLayer=read_int(input, offset),
                  LineIndex=read_int(input, offset),
                  ColorType=read_int(input, offset),
                  CutDirection=read_int(input, offset),
                  # New in V3
                  GameplayType=read_int(input, offset),
                  ScoringType=read_int(input, offset),
                  CutDirectionAngleOffset=read_float(input, offset) 
                  )


def read_height_change(input, offset):
    return HeightEvent(Height=read_float(input, offset),
                       Time=read_float(input, offset))


def read_score_event(input, offset):
    return ScoreEvent(Score=read_int(input, offset),
                      Time=read_float(input, offset),
                      # New in V3
                      ImmediateMaxPossibleScore=read_int(input, offset)
                      )


def read_combo_event(input, offset):
    return ComboEvent(Combo=read_int(input, offset),
                      Time=read_float(input, offset))


def read_multiplier_event(input, offset):
    return MultiplierEvent(Multiplier=read_int(input, offset),
                           NextMultiplierProgress=read_float(input, offset),
                           Time=read_float(input, offset))


def read_energy_event(input, offset):
    return EnergyEvent(Energy=read_float(input, offset),
                       Time=read_float(input, offset))
