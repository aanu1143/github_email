# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-06-23 00:22:41
# @Last Modified by:   prabhakar
# @Last Modified time: 2016-06-23 00:55:10

import requests
import sys

GITHUB_URL = "https://api.github.com/users/"

def main():
    username = sys.argv[1]
    events_url = "https://api.github.com/users/{0}/repos?type=owner&sort=updated".format(username)
    url = GITHUB_URL + username

    response = requests.get(events_url)
    import ipdb; ipdb.set_trace()
    print response
    # response_line_list = response.content.splitlines()

    
    # if(len(sys.argv) > 1):
        
        # for i in languages_list:
            # print i
    # else:
        # print languages_list
        

    # languages_list = []

    # print_flag = False
    # for line in response_line_list:
    #     line = line.strip()
    #     if print_flag:
    #         line = line[:len(line)-1]
    #         languages_list.append(line)
    #         print_flag = False
    #     if line == '':
    #         print_flag = True
    


if __name__ == "__main__":
    main()



    https://api.github.com/users/prabhakar267
    https://api.github.com/users/prabhakar267/repos?type=owner&sort=updated
    https://api.github.com/repos/prabhakar267/github-classifier/commits
    https://gist.github.com/sindresorhus/4512621