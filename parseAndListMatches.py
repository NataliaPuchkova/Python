#!/usr/bin/env python
# encoding: utf
#
# Simple imitation of the Unix find command, which search sub-tree
# for a named file, both of which are specified as arguments.
# Because python is a scripting language, and because python
# offers such fantastic support for file system navigation and
# regular expressions, python is very good at for these types
# of tasks

from sys import argv
from os import listdir
from os.path import isdir, exists, basename, join

def listAllExactMatches(path, filename):
     """Recursive function that lists all files matchingthe specified file name"""
    if (basename(path) == filename):
        print "%s" % path
    if (not isdir(path)):
        return
    dirlist = listdir(path)
    for file in dirlist:
        listAllExactMatches(join(path, file), filename)
def  parseAndListMatches():
    """Parses the command line, confirming that there are in fact three arguments, confirms that the specified path is actually
    the name of a real directory, and then recursively search the file tree rooted at the speci fied directory."""
    if (len(argv) != 3):
        print "Usage: find <path-to-directory-tree> <filename>"
        return    
    directory = argv[1]
    if (not exists(directory)):
        print "Specified path \"%s\" does not exist." % directory
 return;
    if (not isdir(directory)):
        print "\"%s\" exists, but doesn't name an actual directory." % directory
    filename = argv[2]
    listAllExactMatches(directory, filename)
parseAndListMatches()
