# mmRandomizer

The script to randomize career start in Motorsport Manager (PC). It provides randomization for:

* Calendar (races count & order);
* Championships rules;
* Stats of the teams & their cars;
* Names, avatars, stats of the drivers, mechanics, engineers etc.;
  * Including the drivers you get in "create your own team" mode;
  * ONLY FEMALES are generated (my personal wish).

Some things are changed but not randomized, for example the number of teams in each championship (WMC: 12, APC: 10, ERS: 8).

All these changes lead to a more interesting play each time you create the new career.

See the more in-depth description in the `README (generator).md` file.

## IMPORTANT

As I know you <u>should</u> have the endurance series DLC to use the generated files. This DLC brought to the game the updated track models (mainly the garages for 12 teams) and maybe some other systems. Maybe the modded files will work even without endurance DLC, <u>I don't know</u>.

# Usage

1. Extract all the text assets from the original `resources.assets` file. You can use any tool for this purpose or my another script: https://github.com/Kycko/mmExtractor;
2. Add the executable bit for this script: `chmod +x ./mmRandomizer.py`;
3. Run the script with the path to the directory with your extracted original data (where all the `.txt` files are): `./mmRandomizer.py PATH`;
4. If the script finishes with no errors, you will see a bunch of `.txt` files in the `result_***` subdirectory.

## What to do with the created files

1. To use in the game, you should copy them into `.../SteamLibrary/steamapps/common/Motorsport Manager/MM_Data/Modding/Databases/`:
   * Feel free to create this directories if they aren't yet;
   * You can copy all the created files or cherry-pick only the ones you want, but remember some files require another ones, some don't:
     * For example, if you use the `Championships.txt` file but don't want to use `Default Parts.txt`, you will get 12 teams in WMC, but the teams 11 & 12 will have VERY low car performance because it is defined in `Default Parts.txt`. Possible solutions here:
       * Edit `libs/globalsGenerator.py` file to restore the number of teams (10-10-10), but to get random calendars. See the Teams section of `README (generator).md`;
       * Run the script, but then manually edit the generated `Championships.txt` file to move the teams in the corresponding championships;
     * The game will use it's built-in files for the ones you haven't copied (this is the reason of conflicts when some files are copied without another ones);
     * Anyway the game won't freeze, you will just see a message saying the mod can't be loaded;
2. Launch the game, START THE NEW CAREER (this files will not work in the previous saves);
3. Enable your own's mod testing on the very first screen after clicking the new game button.

# License info

License: GPL-3.0-or-later

Author: Anton Samartsev (ant.samarcev@gmail.com)
