# Summary

This file describes all the changes this script will generate for the game (I hope I haven't forgot something).

# Calendars

| championship | number of race weekends | doubles allowed (one country twice) | regions allowed |
| --- | --- | --- | --- |
| WMC   | 16 | NO | all |
| APC   | ERS +1 or +2 with additional conditions (so it will be 9-12) | YES | only non-Europe |
| ERS   | 8-11 | YES | only Europe |
| IGTC  | GTCS +1 or +2 or +3 with additional conditions (so it will be 9-13) | NO | all |
| GTCS  | 8-11 | YES | all |
| IEC-A | 8-10 | NO | all |
| IEC-B | the whole calendar always `== IEC-A` | NO | all |

Additional checks:
* If doubles allowed, there must be at least two other countries between
* Doubles allowed only in the different halves of the season

Editing this generator needs in-depth code changes.

# Championship rules

The script uses weight-based randomization so the different rules have different chances.

You can change this weights by editing the `libs/globalsGenerator.py` file, `rules` dictionary. Be careful here since this can lead to the game unable to load your generated rules.

### Points system

| rule                     | WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B |
| ---                      | ---  | ---  | ---  | ---  | ---  | ---   | ---   |
| top 5                    |   6% |  18% |   0% |   4% |   1% |    9% |    1% |
| top 6                    |  12% |  37% |  13% |  20% |  16% |   13% |   11% |
| top 8                    |  31% |  27% |  15% |  24% |  13% |   32% |   14% |
| top 10                   |  51% |  18% |  11% |  38% |  14% |   34% |   18% |
| top 20                   |   0% |   0% |  61% |  14% |  56% |   12% |   56% |
| final race double points |   3% |  27% |  47% |   7% |  22% |   37% |   45% |
| fastest lap bonus        |  31% |  14% |  49% |  23% |   6% |   10% |   10% |
| pole position bonus      |  28% |  13% |  49% |  27% |  14% |    7% |    7% |

### Session lengths

| rule                       | WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B |
| ---                        | ---  | ---  | ---  | ---  | ---  | ---   | ---   |
| practice length : short    |   0% |   0% | 100% |   0% |  52% |    0% |    0% |
| practice length : medium   |   0% | 100% |   0% |  52% |  48% |    0% |    0% |
| practice length : long     | 100% |   0% |   0% |  48% |   0% |  100% |  100% |
| qualifying length : short  |   0% |   0% | 100% |   0% |  50% |    0% |    0% |
| qualifying length : medium |   0% | 100% |   0% |  50% |  50% |    0% |    0% |
| qualifying length : long   | 100% |   0% |   0% |  50% |   0% |  100% |  100% |
| race length : short        |   0% |   0% | 100% |   0% |  43% |  `NA` |  `NA` |
| race length : medium       |   0% | 100% |   0% |  43% |  57% |  `NA` |  `NA` |
| race length : long         | 100% |   0% |   0% |  57% |   0% |  `NA` |  `NA` |
| time-based race length     |   0% |   0% |   0% |   0% |   0% |  100% |  100% |

### Races

| rule                                | WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B      |
| ---                                 | ---  | ---  | ---  | ---  | ---  | ---   | ---        |
| grid order : qualifying, 3 sessions |  50% |  10% |   0% |  50% |  10% |  `NA` |       `NA` |
| grid order : qualifying, 1 session  |  50% |  40% |  10% |  50% |  30% |  `NA` |       `NA` |
| grid order : random                 |   0% |  10% |  22% |   0% |  30% |  `NA` |       `NA` |
| grid order : reversed               |   0% |  40% |  68% |   0% |  30% |  `NA` |       `NA` |
| start : standing on the grid        | 100% |  77% |  49% |  78% |  50% |   9%  | `== IEC-A` |
| start : moving                      |   0% |  23% |  51% |  22% |  50% |  91%  | `== IEC-A` |
| safety cars : only virtual          |  17% |  47% |   6% |  16% |   1% |  40%  | `== IEC-A` |
| safety cars : only real             |  54% |  44% |  77% |  53% |  93% |  28%  | `== IEC-A` |
| safety cars : both virtual and real |  29% |   9% |  17% |  31% |   6% |  32%  | `== IEC-A` |
| sprinklers active                   |   0% |   0% |   0% |   0% |   0% |   0%  | `== IEC-A` |

### Drivers

| rule                                   | WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B |
| ---                                    | ---  | ---  | ---  | ---  | ---  | ---   | ---   |
| Aids allowed                           |  15% |  40% |  81% |   7% |   6% |  54%  |   87% |
| driving limit : 40% of the race length |   0% |   0% |   0% |   0% |   0% |  45%  |   50% |
| driving limit : 55% of the race length |   0% |   0% |   0% |   0% |   0% |  55%  |   50% |

### Pit-stops

| rule                      | WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B      |
| ---                       | ---  | ---  | ---  | ---  | ---  | ---   | ---        |
| pit-lane speed : 50 MPH   |  30% |  55% |  72% |  34% |  74% |  48%  | `== IEC-A` |
| pit-lane speed : 70 MPH   |  70% |  45% |  28% |  66% |  26% |  52%  | `== IEC-A` |
| sequental pit-stops       |   4% |  31% |  73% |  25% |  80% |  21%  |        75% |
| semi-sequental pit-stops  |  22% |  29% |  20% |  36% |  16% |  36%  |        20% |
| simultaneous pit-stops    |  74% |  40% |   7% |  39% |   4% |  43%  |         5% |
| refuelling : 70 kg tanks  |   0% |   0% |   0% |   0% |   0% |  58%  |        54% |
| refuelling : 140 kg tanks |   0% |   0% |   0% |   0% |   0% |  42%  |        46% |
| refuelling : 40 kg tanks  |   5% |  16% |  68% |  58% |  21% |   0%  |         0% |
| refuelling : 80 kg tanks  |  27% |  68% |  27% |  21% |  58% |   0%  |         0% |
| refuelling : NO           |  68% |  16% |   5% |  21% |  21% |   0%  |         0% |

### Money

| rule                                                | WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B |
| ---                                                 | ---  | ---  | ---  | ---  | ---  | ---   | ---   |
| post-season prizes diff : very high                 |  25% |  12% |   4% |   4% |   7% |   9%  |    6% |
| post-season prizes diff : high                      |  40% |  43% |  34% |  55% |  33% |  49%  |   38% |
| post-season prizes diff : standard                  |  27% |  35% |  38% |  29% |  44% |  35%  |   30% |
| post-season prizes diff : equal                     |   8% |  10% |  24% |  12% |  16% |   7%  |   26% |
| last place bonus                                    |  11% |  14% |  52% |   6% |  52% |  10%  |   17% |
| promotion bonus on going to the better championship |   0% |   0% |   0% |   0% |   0% |   0%  |    0% |

### Car parts

Additional check:

* GT series should have no more than 2 special parts
* Other championships should have no more than 3 special parts

| rule                | WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B |
| ---                 | ---  | ---  | ---  | ---  | ---  | ---   | ---   |
| special engines     |   4% |  16% |  28% |  12% |  28% |   7%  |   30% |
| special gearboxes   |   5% |  13% |  26% |  14% |  39% |   5%  |   39% |
| special front wings |   9% |  17% |  44% | `NA` | `NA` |   4%  |   25% |
| special rear wings  |   6% |  17% |  25% |  14% |  23% |   1%  |   29% |
| special suspensions |   4% |  10% |  29% |  13% |  37% |   8%  |   25% |
| special brakes      |   4% |  13% |  32% |  23% |  31% |   4%  |   28% |
| weight stripping    |  50% |  50% |  10% |  50% |  50% |   0%  |    0% |

### Tyres

| rule                              | WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B |
| ---                               | ---  | ---  | ---  | ---  | ---  | ---   | ---   |
| type : slick, normal width        |  40% |  41% |  29% |  82% |  73% |  25%  |   22% |
| type : slick, wide                |  41% |  10% |   8% |   3% |   2% |  46%  |    3% |
| type : grooved                    |  16% |  38% |  29% |  13% |   9% |  24%  |   37% |
| type : low profile                |   3% |  10% |   1% |   2% |   2% |   5%  |    3% |
| type : road                       |   0% |   1% |  33% |   0% |  14% |   0%  |   35% |
| supplier : Nespola                |  50% |  62% |  62% |  52% |  46% |  44%  |   49% |
| supplier : Kadai                  |  50% |  38% |  38% |  48% |  54% |  56%  |   51% |
| compound choice : free            |  79% |  30% |   3% |  26% |   5% |  75%  |   49% |
| compound choice : pre-distributed |  21% |  70% |  97% |  74% |  95% |  25%  |   51% |
| dry compounds available : 2       |  22% |  52% |  93% |  78% |  99% |  13%  |   47% |
| dry compounds available : 3       |  78% |  48% |   7% |  22% |   1% |  87%  |   53% |
| total amount per weekend : 9      |  20% |  41% |  58% |  74% |  80% |   0%  |    0% |
| total amount per weekend : 12     |  42% |  39% |  30% |  23% |  19% |   0%  |    0% |
| total amount per weekend : 15     |  38% |  20% |  12% |   3% |   1% | 100%  |  100% |

### Energy recovery systems

| rule                                     | WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B |
| ---                                      | ---  | ---  | ---  | ---  | ---  | ---   | ---   |
| ERS : allowed, choose one of 3 types     |   4% |   2% |   0% |  25% |  25% |  25%  |   25% |
| ERS : allowed, 60 kWh                    |   7% |   5% |   3% |  25% |  25% |  25%  |   25% |
| ERS : allowed, 100 kWh                   |  10% |   7% |   4% |  25% |  25% |  25%  |   25% |
| ERS : not allowed                        |  79% |  86% |  93% |  25% |  25% |  25%  |   25% |
| hybrid mode (chosen only if ERS allowed) |  54% |  18% |  10% |   6% |   7% |  81%  |   73% |
| standings based batteries                |   0% |   0% |   0% |   0% |   0% |   0%  |    0% |

# Teams

The number of teams in each championship is changed but not randomized:

| WMC  | APC  | ERS  | IGTC | GTCS | IEC-A | IEC-B |
| ---  | ---  | ---  | ---  | ---  | ---   | ---   |
|   12 |   10 |    8 |   11 |    9 |     6 |     6 |

You can change this pre-defined values by editing the `libs/globalsGenerator.py` file, `champs` dictionary. See the `teams` value for each championship.


Be careful here:
  * Seems the game can not simulate more than 12 teams on one track
  * Endurance series have much more complex simulation because the both series are racing together, so changing these numbers for IEC-A & IEC-B may lead to unexpected bugs
  * <u>WARNING</u>: 11 and 12 teams allowed only for WMC + both GT series
    * APC & ERS with these numbers will raise an error
      * Making this possible needs additional code writing to generate good stats for the commands, but this is not what I'm interested in

## Car parts

I don't want to randomize the cars stats because I want the same original balance, with the same teams winning races, the same middles etc. This is primarily because we all know the reference teams for each one (for example, Ferrari for Rossini) and I don't want to see such teams in the end of the table.

The only thing the script will do is fine-tuning to match the changed number of teams in each championship:

* No changes for ERS teams because we get the last 8 ones and can use the same numbers
* All the stats for APC teams (teams 11-20) are copied to the new teams (13-22): from team 12 to team 14, from team 17 to team 19 etc.
* Teams 11 & 12 are now in WMC so they will get the new stats matching WMC level
* No changes for GT series because the stats of the last IGTC teams are equal with the stats of the first GTCS teams
* No changes for endurance series because the number of teams stays unchanged
