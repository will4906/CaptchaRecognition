import os
import requests

captcha_url = 'https://user.lu.com/user/captcha/captcha.jpg'

if __name__ == '__main__':
    save_dir = 'source'
    if os.path.exists(save_dir) is False:
        os.mkdir(save_dir)

    for i in range(1000):
        resp = requests.get(captcha_url)
        with open(save_dir + os.sep + 'captcha_%d.jpg' % (i), 'wb') as f:
            f.write(resp.content)
