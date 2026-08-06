def build_filter(args):
    return Filter(args)

class Filter:
    def __init__(self, _):
        pass

    def commit_message_filter(self, commit_data):
        hg_hash = commit_data['hg_hash']
        if hg_hash is not None:
            commit_data['desc'] = (
                    commit_data['desc'] + b'\n\nhg hash: ' + hg_hash 
            )

