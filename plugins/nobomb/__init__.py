def build_filter(args):
    return Filter(args)


class Filter:

    def __init__(self, args):
        pass

    def file_data_filter(self, file_data):

        if file_data.get('is_largefile'):
            if b'\0' in file_data['data']:
                return

        file_ctx = file_data['file_ctx']

        if file_ctx is None:
            return

        if file_ctx.isbinary():
            return

        if file_data['data'][:3] == b'\xef\xbb\xbf':
            file_data['data'] = file_data['data'][3:]

