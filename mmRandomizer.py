#!/usr/bin/python3

from sys import path
path.append('libs')
import files as F

# значения в files{} = объекты классов типа Championships, Tracks, ...
files = F.readAll()
files['champ'].genTracks(files['tracks'])
F.writeAll(files)
