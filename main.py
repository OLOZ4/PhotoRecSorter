import os
recup_dir = "Documents/recup_dir." # path to your recup directories. Make sure, that it ends with recup_dir. 
destination = "Documents/" # change it to your destination directory. 
i = 0
k = 6024 # change it to number of recup directories you have.
file_types =["", "flv", "tex", "xcf", "apk", "ai", "3gp", "bat", "xz", "tz", "jsonlz4", "json",
"pcx", "zip", "jpg", "h", "class", "pct", "priv", "mpg", "DS_Store", "wtv", "gif", "dex", "au",
"psd", "fits", "mbox", "lzo", "ttf", "wav", "pap", "html", "rpm", "aif", "a", "c", "sh", "bz2",
"bmp", "woff", "xmp", "cab", "bpg", "wim", "ico", "mp3", "swc", "swf", "reg", "edb", "mkv", "go",
"ppm", "cr2", "wpl", "ifo", "pfx", "icc", "mid", "dng", "one", "ps", "rns", "jsp", "ibd", "wma",
"xpt", "mdb", "iso", "emf", "djv", "asp", "f", "sqlite", "icns", "dat", "mlv", "sxw", "dll",
"epub", "m3u", "map", "ogg", "pcap", "cdt", "evtx", "pub", "ini", "m4p", "pgm", "wld", "eps",
"torrent", "tif", "sqm", "ab", "jar", "pl", "tar", "MYI", "wmv", "csv", "lit", "key", "jks",
"ldif", "notebook", "dxf", "7z", "ics", "pyc", "chm", "lnk", "amr", "webp", "gpg", "pdf",
"rb", "db", "flac", "wmf", "py", "ods", "java", "svg", "wps", "php", "xml", "accdb", "pm",
"plist", "elf", "exe", "blend", "rtf", "inf", "res", "apple", "rar", "webm", "avi", "fods",
"odt", "ani", "nef", "gz", "deb"] 
# these are the file extentions that will be checked in recup_dir.* folders, alternatively you could use extention_finder.py script in my repository to speed up the process.
for file_type in file_types: # creates directory for every file type listed in "file_types".
    destination_directory = destination + file_type
    os.system("mkdir -p " + destination_directory) 

    for i in range(k): # moves all files with matching extention to folder named after that extenton.
        source_directory = recup_dir + str(i+1)
        os.system("sudo mv -v " + source_directory + "/*." + file_type + " " + destination_directory + "/") 

    if len(os.listdir(destination_directory)) == 0: # remove any leftover folders that have 0 files in them
        os.system("rmdir " + destination_directory) 
