# dev-nag-bot
A nag/joke tool for git. recipients reminders to document changes to chosen git repositories.

# How it works
-Developer A edits some component of the GUI in an app
-Developer A forgets to document the change
-nag-bot(running weekly) reviews commits from last it ran
-nag-bot finds that 25 files of interest were changed by Developer A
-nag-bot shoots out a joke email asking about the 25 GUI files in the repository have been changed, with file names, commit messages and other authors

Works on multiple repositories at a time.

# install gitpython
pip install gitpython

# clone this repo
git clone https://github.com/spelexander/dev-nag-bot.git

# enter to repo
cd dev-nag-bot

# run
python nagger.py

# Edit the config.json file for the desired attributes:
{
  "UserName":"enter-email@gmail.com", # Gmail account email address to use
  "Sender":[ # Arbitrary joke list of names to randomly select from to set as the senders name
  "Fergus",
  "Henry",
  "Bob",
  "Alice"
  ],
  "Password":"enter-password", # Gmail account password to use
  "To":[
    "enter-recepient@email.com" # Who to send it to!
  ],
  "Repos":[
    "/path/to/repo" # Path the repo's you want to the tool to follow
  ],
  "Apps":[ # App names associated with the repo's (for formatting purposes)
    "app1", 
    "app2"
  ],
  "CommitCount":50, # How many commits to look back on
  "Branch":"master", # Which branch to follow
  "DateFile":"previous-date.txt", # where to persist last time this ran
  "Extensions": [ # which file types to watch
    ".java",
    ".py",
  ],
  "Packages":[ # Which fragments (or full names) of files to associate with a UI change
    "Panel",
    "Model",
    "Dialog",
  ]

# Now put it in a cronjob to pull from other repo's and run at your own discretion
