from enum import Enum
import math


class Pointers:
    def __init__(self,
                 metadata=0,
                 poseKeyframes=0,
                 heightKeyframes=0,
                 noteKeyframes=0,
                 scoreKeyframes=0,
                 comboKeyframes=0,
                 multiplierKeyframes=0,
                 energyKeyframes=0,
                 fpsKeyframes=0):
        self.metadata = metadata
        self.poseKeyframes = poseKeyframes
        self.heightKeyframes = heightKeyframes
        self.noteKeyframes = noteKeyframes
        self.scoreKeyframes = scoreKeyframes
        self.comboKeyframes = comboKeyframes
        self.multiplierKeyframes = multiplierKeyframes
        self.energyKeyframes = energyKeyframes
        self.fpsKeyframes = fpsKeyframes


class ReplayData:
    def to_dict(self) -> dict:
        return dict(self)

    def __repr__(self) -> str:
        return repr(self.to_dict())


class Metadata(ReplayData):
    def __init__(self,
                 Version="",
                 LevelID="",
                 Difficulty=0,
                 Characteristic="",
                 Environment="",
                 Modifiers=[],
                 NoteSpawnOffset=0.0,
                 LeftHanded=False,
                 InitialHeight=0.0,
                 RoomRotation=0.0,
                 RoomCenter=None,
                 FailTime=0.0):
        self.Version = Version
        self.LevelID = LevelID
        self.Difficulty = Difficulty
        self.Characteristic = Characteristic
        self.Environment = Environment
        self.Modifiers = Modifiers
        self.NoteSpawnOffset = NoteSpawnOffset
        self.LeftHanded = LeftHanded
        self.InitialHeight = InitialHeight
        self.RoomRotation = RoomRotation
        self.RoomCenter = RoomCenter
        self.FailTime = FailTime

    def to_dict(self):
        return {
            'Version': self.Version,
            'LevelID': self.LevelID,
            'Difficulty': self.Difficulty,
            'Characteristic': self.Characteristic,
            'Environment': self.Environment,
            'Modifiers': self.Modifiers,
            'NoteSpawnOffset': self.NoteSpawnOffset,
            'LeftHanded': self.LeftHanded,
            'InitialHeight': self.InitialHeight,
            'RoomRotation': self.RoomRotation,
            'RoomCenter': self.RoomCenter,
            'FailTime': self.FailTime,
        }


class ScoreEvent(ReplayData):
    def __init__(self, Score=None, Time=None, ImmediateMaxPossibleScore=None):
        self.Score = Score
        self.Time = Time
        self.ImmediateMaxPossibleScore = ImmediateMaxPossibleScore

    def to_dict(self):
        return {
            'Score': self.Score,
            'Time': self.Time,
            'ImmediateMaxPossibleScore': self.ImmediateMaxPossibleScore,
        }


class ComboEvent(ReplayData):
    def __init__(self, Combo=None, Time=None):
        self.Combo = Combo
        self.Time = Time

    def to_dict(self):
        return {
            'Combo': self.Combo,
            'Time': self.Time,
        }


class NoteEvent(ReplayData):
    def __init__(self,
                 NoteID=None,
                 EventType=None,
                 CutPoint=None,
                 CutNormal=None,
                 SaberDirection=None,
                 SaberType=None,
                 DirectionOK=None,
                 SaberSpeed=None,
                 CutAngle=None,
                 CutDistanceToCenter=None,
                 CutDirectionDeviation=None,
                 BeforeCutRating=None,
                 AfterCutRating=None,
                 Time=None,
                 UnityTimescale=None,
                 TimeSyncTimescale=None,
                 # New in V3
                 TimeDeviation=None,
                 WorldRotation=None,
                 InverseWorldRotation=None,
                 NoteRotation=None,
                 NotePosition=None,
                 ):
        self.NoteID = NoteID
        self.EventType = EventType
        self.CutPoint = CutPoint
        self.CutNormal = CutNormal
        self.SaberDirection = SaberDirection
        self.SaberType = SaberType
        self.DirectionOK = DirectionOK
        self.SaberSpeed = SaberSpeed
        self.CutAngle = CutAngle
        self.CutDistanceToCenter = CutDistanceToCenter
        self.CutDirectionDeviation = CutDirectionDeviation
        self.BeforeCutRating = BeforeCutRating
        self.AfterCutRating = AfterCutRating
        self.Time = Time
        self.UnityTimescale = UnityTimescale
        self.TimeSyncTimescale = TimeSyncTimescale
        self.TimeDeviation = TimeDeviation
        self.WorldRotation = WorldRotation
        self.InverseWorldRotation = InverseWorldRotation
        self.NoteRotation = NoteRotation
        self.NotePosition = NotePosition

    def to_dict(self):
        return {
            'NoteID': self.NoteID,
            'EventType': self.EventType,
            'CutPoint': self.CutPoint,
            'CutNormal': self.CutNormal,
            'SaberDirection': self.SaberDirection,
            'SaberType': self.SaberType,
            'DirectionOK': self.DirectionOK,
            'SaberSpeed': self.SaberSpeed,
            'CutAngle': self.CutAngle,
            'CutDistanceToCenter': self.CutDistanceToCenter,
            'CutDirectionDeviation': self.CutDirectionDeviation,
            'BeforeCutRating': self.BeforeCutRating,
            'AfterCutRating': self.AfterCutRating,
            'Time': self.Time,
            'UnityTimescale': self.UnityTimescale,
            'TimeSyncTimescale': self.TimeSyncTimescale,
            'TimeDeviation': self.TimeDeviation,
            'WorldRotation': self.WorldRotation,
            'InverseWorldRotation': self.InverseWorldRotation,
            'NoteRotation': self.NoteRotation,
            'NotePosition': self.NotePosition,
        }


class NoteEventType(Enum):
    NoneType = 0
    GoodCut = 1
    BadCut = 2
    Miss = 3
    Bomb = 4


class NoteID(ReplayData):
    def __init__(self,
                 Time=None,
                 LineLayer=None,
                 LineIndex=None,
                 ColorType=None,
                 CutDirection=None,
                 # New in V3
                 GameplayType=None,
                 ScoringType=None,
                 CutDirectionAngleOffset=None,
                 ):
        self.Time = Time
        self.LineLayer = LineLayer
        self.LineIndex = LineIndex
        self.ColorType = ColorType
        self.CutDirection = CutDirection
        self.GameplayType = GameplayType
        self.ScoringType = ScoringType
        self.CutDirectionAngleOffset = CutDirectionAngleOffset

    def __eq__(self, other):
        return math.isclose(self.Time, other.Time) and self.LineIndex == other.LineIndex and self.LineLayer == other.LineLayer and self.ColorType == other.ColorType and self.CutDirection == other.CutDirection

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.Time, self.LineLayer, self.LineIndex))

    def to_dict(self):
        return {
            'Time': self.Time,
            'LineLayer': self.LineLayer,
            'LineIndex': self.LineIndex,
            'ColorType': self.ColorType,
            'CutDirection': self.CutDirection,
            'GameplayType': self.GameplayType,
            'ScoringType': self.ScoringType,
            'CutDirectionAngleOffset': self.CutDirectionAngleOffset,
        }


class EnergyEvent(ReplayData):
    def __init__(self, Energy=None, Time=None):
        self.Energy = Energy
        self.Time = Time

    def to_dict(self) -> str:
        return {
            'Energy': self.Energy,
            'Time': self.Time,
        }


class HeightEvent(ReplayData):
    def __init__(self, Height=None, Time=None):
        self.Height = Height
        self.Time = Time

    def to_dict(self) -> str:
        return {
            'Height': self.Height,
            'Time': self.Time,
        }


class MultiplierEvent(ReplayData):
    def __init__(self, Multiplier=None, NextMultiplierProgress=None, Time=None):
        self.Multiplier = Multiplier
        self.NextMultiplierProgress = NextMultiplierProgress
        self.Time = Time

    def to_dict(self) -> str:
        return {
            'Multiplier': self.Multiplier,
            'NextMultiplierProgress': self.NextMultiplierProgress,
            'Time': self.Time,
        }


class VRPoseGroup(ReplayData):
    def __init__(self, Head=None, Left=None, Right=None, FPS=0, Time=0.0):
        self.Head = Head
        self.Left = Left
        self.Right = Right
        self.FPS = FPS
        self.Time = Time

    def to_dict(self) -> str:
        return {
            'Head': self.Head,
            'Left': self.Left,
            'Right': self.Right,
            'FPS': self.FPS,
            'Time': self.Time,
        }


class VRPose(ReplayData):
    def __init__(self, Position=None, Rotation=None):
        self.Position = Position
        self.Rotation = Rotation

    def to_dict(self) -> str:
        return {
            'Position': self.Position,
            'Rotation': self.Rotation,
        }


class VRPosition(ReplayData):
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z

    @staticmethod
    def Origin():
        return VRPosition()

    def to_dict(self):
        return {
            'X': self.X,
            'Y': self.Y,
            'Z': self.Z
        }


class VRRotation(ReplayData):
    def __init__(self, x, y, z, w):
        self.X = x
        self.Y = y
        self.Z = z
        self.W = w

    def to_dict(self):
        return {
            'X': self.X,
            'Y': self.Y,
            'Z': self.Z,
            'W': self.W
        }
