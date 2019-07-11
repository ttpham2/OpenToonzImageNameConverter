# OpenToonzImageNameConverter

Converts image filenames(jpg, png, or tiff) to match Opentoonz's naming convention such that images may be imported as a single level.
Ex: 1.png gets converted to currentDirectory.0001.png, 103.jpg gets converted to currentDirectory.0103.jpg, etc. 

Alternatively, a different name can be passed as a command line argument should you not want the current working directory's name to
precede each filename.
