import requests
import json

PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS']
GROUPS = ['1021', '1022']
ACCOUNTS =['sanchousss']

LOGIN = 'sanchousss'
TOKEN = 'private_info'

def prepare_headers():
    return {
        'Authorization': 'token {}'.format(TOKEN),
        'Content-Type': "application/json",
        'Accept': "application/vnd.github.v3+json"
    }

def prepare_body(pull, comment):
    return {
        'body': f"{comment}",
        'path': requests.get(pull['url'] + '/files', headers=prepare_headers()).json()[0]['filename'],
        'position': 1,
        'commit_id': pull['head']['sha']
    }

def check_prefixes(message):
    message = message.split()
    pref = message[0].split('-')
    if len(pref) != 2:
        return 'ALL WRONG'
    group = pref[1]
    pref = pref[0]
    if group in GROUPS:
        if pref in PREFIXES:
            return 'OKK'
        else:
            return 'WRONG PREFIX'
    else:
        return 'WRONG GROUP'


def get_all_user_prs(user_login, repo_name, pr_state):
    user_login = f'https://api.github.com/repos/{user_login}/{repo_name}/pulls?state={pr_state}'
    res = []
    all_prs = requests.get(user_login)
    for pr in all_prs.json():
          res.append(pr)
    return res

def get_all_commits(pr):
  res = []
  link = requests.get(pr['commits_url'])
  for commit in link.json():
    res.append(commit['commit'])
  return res


def send_pr_comment(pull, comment):
    url = pull['url'] + '/comments'
    print(url)
    r = requests.post(url, headers=prepare_headers(), data=json.dumps(prepare_body(pull, comment)))
    return pull['html_url']

def verify_pr(pr):
    commits = get_all_commits(pr)
    comments = []
    if len(check_prefixes(pr['title'])) > 3:
        comment = check_prefixes(pr['title']) + ' IN PR TITLE'
        comments.append(comment)
    for commit in commits:
        if len(check_prefixes(commit['message'])) > 3:
            comment = check_prefixes(commit['message']) + ' IN COMMIT MESSAGE'
            comments.append(comment)
    if len(comments) != 0:
        send_pr_comment(pr, '\n\n'.join(comments))

def compare_dates(date1, date2):#"2020-10-02T22:06:46Z" ['2020','10','02','22','06','46']
    if date1[0] > date2[0]:
        return date1
    elif date1[0] == date2[0]:
        if date1[1] > date2[1]:
            return date1
        elif date1[1] == date2[1]:
            if date1[2] > date2[2]:
                return date1
            elif date1[2] == date2[2]:
                if date1[3] > date2[3]:
                    return date1
                elif date1[3] == date2[3]:
                    if date1[4] > date2[4]:
                        return date1
                    elif date1[4] == date2[4]:
                        if date1[5] > date2[5]:
                            return date1
                        elif date1[5] == date2[5]:
                            return 0
    return date2

def find_date(all_prs):
    M = ['0','0','0','0','0','0']
    for pr in all_prs:
        comments = requests.get(pr['review_comments_url']).json()
        #print(comments)
        for comment in comments:
            if comment['user']['login'] == LOGIN:
                new_date = comment['created_at']
                new_date = new_date.split('-')
                new_date.append(new_date[2][:2])
                new_date.append(new_date[2][3:-7])
                new_date.append(new_date[2][6:-4])
                new_date.append(new_date[2][9:-1])
                new_date.pop(2)
                M = compare_dates(M, new_date)
                print(M)

if __name__ == '__main__':
    date = ['0','0','0','0','0','0']
    repo_name = 'python_au'
    pr_state = 'open'
    all_prs = get_all_user_prs('vasis3038', repo_name, pr_state)
    lst = [all_prs[0], all_prs[1], all_prs[2]]
    find_date(lst)
    for acc in ACCOUNTS:
        all_prs = get_all_user_prs(acc, repo_name, pr_state)
        date = find_date(all_prs)
        for pr in all_prs:
            if compare_dates(pr['created_at'], date) != date:
                verify_pr(pr)