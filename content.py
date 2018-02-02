import random

class content:

    def __init__(self):
        self.content = "<div>What!?</div><br><div>It's only been like $DAYS since I last checked and it looks like $AUTHORS " \
                       "changed the UI for $APPS $TIMES times!</div> \
        <div></div> \
        <ul>$APP_CONTENT</ul> \
        <div></div> \
        <div>But what was changed?!</div><br> \
        <div></div> \
        <div>Sincerely,</div> \
        <div>$SENDER</div>"

    def get_content(self):
        return self.content

    def format_content(self, days, authors, apps, app_contents, messages, senders):
        if len(app_contents) is 0:
            return None

        sender = senders[random.randint(0, len(senders) - 1)]

        app_content = ""
        for i, a in enumerate(app_contents):
            app_content += "<li><strong>" + a.split(".")[0] + "</strong>   ->   " +  messages[i] + "</li>"

        daystring = str(days) + " days"

        times = str(len(app_contents))

        authorString = " & ".join(authors)
        if len(authors) is  1:
            authorString += " has"
        else:
            authorString += " have"

        result = self.get_content()
        result = result.replace("$DAYS", daystring)
        result = result.replace("$TIMES", times)
        result = result.replace("$AUTHORS", authorString)
        result = result.replace("$APPS", "/".join(apps))
        result = result.replace("$APP_CONTENT", app_content)
        result = result.replace("$SENDER", str(sender))

        return result