import opml

subscriptions = opml.from_string(open('subscriptions.opml', 'r').read().encode("UTF-8"))


def is_category(item):
    return not hasattr(item, 'type')


def list_feeds(title, clctn, indent=0):
    print((" " * indent) + title)
    for row in clctn:
        if is_category(row):
            list_feeds(row.title, row, indent + 1)
        else:
            print((" " * (indent + 1)) + row.title + " " + row.xmlUrl)


list_feeds(subscriptions.title, subscriptions)