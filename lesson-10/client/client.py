import requests

BASE_URL = "http://127.0.0.1:8000/"

HEADERS = {"Content-Type": "application/json"}

def get_all_posts():
    all_posts = requests.get(BASE_URL+'posts', params={'limit': 100})
    return all_posts.json()


def get_post(post_id):
    post = requests.get(BASE_URL+f'posts/{post_id}')
    return post.json()

def create_post():
    pass

def update_post(post_id):
    pass

def delete_post(post_id):
    pass

def get_comments_with_params():
    pass

def create_user():
    pass


if __name__ == '__main__':
    post = get_all_posts()[-1]
    print(post)