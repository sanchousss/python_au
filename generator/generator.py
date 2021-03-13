import sys

class LeetCodeSource:
    def __init__(self, title, link, code):
        self.title = title.split('. ')[1].rstrip('\n')
        self.link  = link.rstrip('\n')
        self.code = code

    def __str__(self):
        return 'title = {}, link = {}, code = {}'.format(self.title, self.link, self.code)

    def get_md_solution_link(self):
        return '+[{}](#{})'.format(self.title, self.link[9:-1])

    def get_md_formated_code(self):
        return '```python\n{}\n```'.format('\n'.join(map(lambda x: x.rstrip('\n')[4:], self.code)))

def get_md_title(str):
    return '\n\n## {}'.format(str)

def read_all_lines_from_file(file_name):
    file = open(file_name)
    result = file.readlines()
    file.close()
    return result


def write_to_md(file_name, data):
    file = open(file_name, 'a')
    file.write(data)
    file.close()

def main(src, dst):
    in_text = read_all_lines_from_file(src)
    source = LeetCodeSource(in_text[0], in_text[1], in_text[3:])
    source.code = source.get_md_formated_code()

    md_link = source.get_md_solution_link()
    res = read_all_lines_from_file(dst)
    res.append(get_md_title(source.title)+'\n\n\n')
    res.append(source.link + '\n\n')
    res.append(source.code + '\n')
    res.append(md_link + '\n')

    #print(res)
    for i in range(len(res)):
        write_to_md(dst, res[i])


if __name__ == '__main__':
    params = sys.argv
    main(params[1], params[2])