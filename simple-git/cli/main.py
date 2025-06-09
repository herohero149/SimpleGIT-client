import argparse
from git_core.repo import init_repo
from git_core.index import add_files
from git_core.commit import create_commit
from git_core.network import clone_repo, push_to_remote, fetch_from_remote

def main():
    parser = argparse.ArgumentParser(description="Simple Git Client")
    subparsers = parser.add_subparsers(dest='command')

    # init
    subparsers.add_parser('init', help='Initialize new repo')

    # clone
    clone_parser = subparsers.add_parser('clone', help='Clone remote repository')
    clone_parser.add_argument('url', help='Repository URL')
    clone_parser.add_argument('path', nargs='?', default='.')

    # add
    add_parser = subparsers.add_parser('add', help='Add files to index')
    add_parser.add_argument('files', nargs='+', help='Files to add')

    # commit
    commit_parser = subparsers.add_parser('commit', help='Commit changes')
    commit_parser.add_argument('-m', '--message', required=True, help='Commit message')

    # push
    push_parser = subparsers.add_parser('push', help='Push to remote')
    push_parser.add_argument('--remote', default='origin')
    push_parser.add_argument('--branch', default='main')

    # pull
    pull_parser = subparsers.add_parser('pull', help='Pull from remote')
    pull_parser.add_argument('--remote', default='origin')
    pull_parser.add_argument('--branch', default='main')

    args = parser.parse_args()

    if args.command == 'init':
        init_repo()
    elif args.command == 'clone':
        clone_repo(args.url, args.path)
    elif args.command == 'add':
        add_files(args.files)
    elif args.command == 'commit':
        create_commit(args.message)
    elif args.command == 'push':
        push_to_remote(remote=args.remote, branch=args.branch)
    elif args.command == 'pull':
        fetch_from_remote(remote=args.remote, branch=args.branch)
    else:
        parser.print_help()