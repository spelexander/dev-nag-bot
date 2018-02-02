import os.path as osp
from git import Repo
import sys
from config import config
from content import content
from mailer import mailer

class nagger(object):

    def __init__(self):
        # Config file with indexed packages and previous date read
        self.config = config("config.json")
        self.content = content()
        self.join = osp.join
        self.mailer = mailer(self.config)

        self.data = {}
        self.authors = []
        self.files = []
        self.messages = []

    def nag(self):
        print 'preparing to nag'

        for path in self.config.repos:
            repo = Repo(path)
            assert not repo.bare

        commits = list(repo.iter_commits(self.config.branch, max_count=self.config.commit_count))

        for q,commit in enumerate(commits):
            if not self.config.is_commit_new(commit):
                continue;

            result = self.config.get_ui_changes(commit, self.data)

            if result[0]:
                name = str(commit.committer.name)
                name = name.split(" ")[0]
                if not name in self.authors:
                    self.authors.append(name)

            self.data = result[1]

        print 'Nag prepared to nag.'
        output = self.prepare_output()

        # Send the email
        if not output is None:
            self.mailer.send(output)

        print "Nag sent."
        self.config.done()

    def prepare_output(self):
        # preparing output
        for i,d in enumerate(self.data.keys()):
            self.files.append(str(d))
            self.messages.append(str(self.data[d]))

        # Calculate time diff
        if not self.config.last_date is None:
            c = self.config.current_date - self.config.last_date
            days = c.days

            # Format content
            result = self.content.format_content(days, self.authors, ["KDXplore"], self.files, self.messages, self.config.sender)
            return result

nagger = nagger()
nagger.nag()