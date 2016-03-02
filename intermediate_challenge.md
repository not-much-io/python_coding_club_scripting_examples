
# Challenge for the Intermediate group

## Challenge

*Friend* 
"Damn, my hard drive is a mess!
 I have all these old movies, pictures, files and stuff all around my hard drive!
 They are all messed up and I'm running out of space!"

*You*
 "Pft, I could write a Python script to do that."

## Analyzer

```
python analyzer.py -p "path/to/directory_tree" --conf analyzer_conf.json
```

This script should analyze the folder structure for possible ways to save space based on the configuration given.
It should produce a human readable and modifiable file with a summary.

This is so a user could look it over and make adjustments before feeding this file into the compactor for realization.

The configuration file might contain data like this:

```python
{
    "not_viewed_since"  : {
                            "almost_never_viewed"    : { "timedelta": .., # Timedelta between last read and creation
                                                         "date"     : .., # After when had to be created (avoid new files)
                                                         "action"   : "delete"
                            "hardly_ever_viewed"     : { "date"   : "01.01.2012", # Files not read after this time
                                                         "action" : "zip",
                                                         "ignore_dirs" : [..],  # Optionally ignore these dirs or files
                                                         "ignore_files": [..]}, # for "hardly_ever_viewed"
                            "rarely_viewed"          : { "date"   : "01.01.2014",
                                                         "action" : "none"}
                          }
    # Add more checks if you want. For modified_since, extra large files etc..
}
```

The result file might contain data like this:

```python
{
    "copies"                : {
                                "x.mp3" : ["path/to/x1/x.mp3", 
                                           "path/to/x2/x.mp3"],
                                "action": "keep"
                              }, 
    "almost_never_viewed"   : {
                                "action"        : "delete",
                                "files"         : [..],
                              },
    "hardly_ever_viewed"    : {
                                "action"        : "zip",
                                "files"         : [..],
                              },
    etc.
}
```

The user should be able to manually remove whole chunks of the analysis result and it would run, just skipping the 
missing steps.

## Compactor

```
python compactor.py --conf compactor_conf.json 
```

Should actually realize the processes with the parameters in the analysis results.
If you want, add backup functionality, result transfer to an external disk etc.