from gooey import Gooey, GooeyParser
from subprocess import call


@Gooey(program_name='Internet Video Downloader',required_cols=1)
def parse_args():
    parser = GooeyParser(description='download youtube and bilibili viedo')
    parser.add_argument('url',help="the url of the viedo you want to download")
    parser.add_argument('loc',help="the location where you save the viedo",widget='DirChooser')
    parser.add_argument('--proxy',help="your proxy server",default='""')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    url = args.url
    loc = args.loc
    proxy = args.proxy
    output = '"' + loc + '\%(title)s.%(ext)s' + '"'
    cmd = 'youtube.exe --output ' + output + ' --proxy ' + proxy + " " + url
    call(cmd,shell=True)
