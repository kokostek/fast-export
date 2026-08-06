def build_filter(args):
    return Filter(args)

class Filter():
    def __init__(self, args):
        pass

    def file_data_filter(self,file_data):
        if file_data['file_ctx'] == None:
            return
        if file_data.get('is_largefile'):
            # file_ctx here refers to the .hglf/ pointer file, not the real
            # content, hence file_ctx.isbinary() will not indicate if file is
            # binary or not. So, let's reimplement it inplace:
            if b'\0' in file_data['data']:
                return
        file_ctx = file_data['file_ctx']
        if not file_ctx.isbinary():
            file_data['data'] = file_data['data'].replace(b'\r\n', b'\n')
