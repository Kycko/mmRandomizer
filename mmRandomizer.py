#!/usr/bin/python3

from sys import path
path.append('libs')
import files  as F
import output as O

O.progress.stageTitle('ttlPre')
# значения в files{} = объекты классов типа Championships, Tracks, ...
files = F.readAll()

O.progress.stageTitle('ttlGen')
files['champ'].genTracks(files['tracks'])
files['champ'].genRules (files['rules'])
files['champ'].moveTeams(files['chassis'])

O.progress.stageTitle('ttlFin')
F.writeAll(files)
