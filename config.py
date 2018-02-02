import os.path
from time import mktime
from datetime import datetime
import json
import time

class config(object):

    def __init__(self, path):
        data = json.load(open(path))

        print 'Reading nag details'

        # Reading the config file
        self.packages = data['Packages']
        self.branch = data['Branch']
        self.apps = data['Apps']
        self.repos = data['Repos']
        self.date_file = data["DateFile"]
        self.last_date = None
        self.commit_count = data["CommitCount"]
        self.current_date = datetime.now()
        self.exts = data['Extensions']
        self.format = "%y-%m-%dT%H:%M:%S"

        # Email stuff
        self.sender = data["Sender"]
        self.username = data["UserName"]
        self.password = data["Password"]
        self.to = data["To"]

        if os.path.isfile(self.date_file):
            f = open(self.date_file, "r+")
            lines = f.readlines()
            if len(lines) > 0:
                line = None
                i = len(lines) - 1
                while line is None:
                    if i < 0:
                        break
                    line = lines[i].strip()
                    if not line is None:
                        self.last_date = datetime.strptime(line, self.format)
                    i -= 1
            f.close()
        else:
            f = open(self.date_file, "w+")
            f.close()

    def is_commit_new(self, commit):
        if self.last_date is None:
            return True

        # Check if the commit has not been seen
        date = time.gmtime(commit.committed_date)
        dt = datetime.fromtimestamp(mktime(date))
        if dt > self.last_date:
            return True
        return False

    def get_ui_changes(self, commit, result):

        changed = False

        # We only want specific file types
        for file in commit.stats.files.keys():
            for ext in self.exts:
                if not str(file).endswith(ext):
                    continue

            parts = file.split("/")
            name = parts[len(parts) - 1]

            # We don't want commits which did not change any files
            # changes = commit.stats.files[file]
            # dels = int(changes['deletions'])
            # lins = int(changes['lines'])
            # ins = int(changes['insertions'])
            # if (dels + lins + ins) < 1:
            #     continue

            # We want actual commits only
            if str(commit.message).startswith("Merge"):
                continue

            for check in self.packages:
                if check in name:
                    result[name.strip()] = str(commit.message)
                    changed = True

        return (changed, result)

    def done(self):
        f = open(self.date_file, "a+")
        f.write(self.current_date.strftime(self.format) + "\n")
        f.close()


