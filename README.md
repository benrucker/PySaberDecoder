# PySaberDecoder

A Score Saber replay decoder written in Python.

⚠ very WIP! ⚠

### Planned features

- Full decode support for Score Saber replay files
- CSV & JSON support
- Super easy usage & configuration

## Usage

1. Download this project
   - You can do this by clicking the green "Code" button in the top right and clicking "Download ZIP"
   - Or (recommended) use `git`

```sh
git clone https://github.com/benrucker/PySaberDecoder.git
```

2. `cd` into the project directory

```sh
cd PySaberDecoder
```

3. Run the program

```sh
python main.py -i path/to/your/input.dat -i path/to/the/output.csv
```

## Maintaining this project

This project was written initially to support ScoreSaber replay files V2 and then updated to work exclusively with V3.

Whenever ScoreSaber updates how replay files are saved, you'll need to add or remove any fields that were changed in [this file](https://github.com/ScoreSaber/scoresaber-plugin/blob/5c4ec68d472d53df66e3530099752b1567471c64/ScoreSaber/Core/ReplaySystem/Data/ReplayFile.cs) (if the link is broken, look for `ReplayFile.cs` in the [scoresaber-plugin](https://github.com/ScoreSaber/scoresaber-plugin) repo).

Feel free to make the change yourself and then open a pull request to add it to the project! I'd appreciate it 😉
