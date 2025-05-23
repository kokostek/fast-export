def build_filter(args):
    return Filter(args)


def filter_line(line):
    if line == b'/bin/':
        return b'bin/'
    if line == b'/obj/':
        return b'obj/'
    if line == b'syntax: glob':
        return None
    return line


class Filter:

    def __init__(self, args):
        pass

    def file_data_filter(self, file_data):

        if file_data['filename'] != b'.hgignore':
            return

        data = file_data['data']

        if data[:3] == b'\xef\xbb\xbf':
            bom, data = data[:3], data[3:]
        else:
            bom, data = b'', data

        original_lines = data.split(b'\r\n')
        filtered_lines = map(filter_line, original_lines)

        new_data = b'\r\n'.join(
            line for line in filtered_lines
            if line is not None
        )

        file_data['filename'] = b'.gitignore'
        file_data['data'] = bom + new_data

