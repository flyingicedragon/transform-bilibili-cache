import argparse
import files_scanner

arg_parser = argparse.ArgumentParser(
    description='提取安卓平台旧版 BiliBili 客户端（测试版本：5.37.0）缓存视频')
arg_parser.add_argument(
    '--cache-path',
    '-c',
    type=str,
    dest='cache_path',
    help='缓存视频根目录'
)
arg_parser.add_argument(
    '--out-path',
    '-o',
    type=str,
    dest='out_path',
    help='提取结果输出目录'
)
args = arg_parser.parse_args()

files_scanner.Cache(args.cache_path, args.out_path)
