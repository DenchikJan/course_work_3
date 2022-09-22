from flask import render_template, Blueprint, redirect
from utils import Posts, Comments, add_post_in_bookmarks, del_post_from_bookmarks, read_file, posts_wish_teg

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')

file_posts = 'data/posts.json'
file_comments = 'data/comments.json'
file_bookmarks = 'data/bookmarks.json'

class_posts = Posts(file_posts)
class_comments = Comments(file_comments)


@bookmarks_blueprint.route('/add/<int:post_id>')
def add_post(post_id):
    """���������� ����� � ���������, �� ��������!"""
    new_post = class_posts.get_post_by_pk(post_id)
    add_post_in_bookmarks(new_post)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/del/<int:post_id>')
def del_post(post_id):
    """�������� ����� �� ����������"""
    del_post_from_bookmarks(post_id)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/')
def get_bookmarks_posts():
    """�������� � ������� ����������� � ���������"""
    posts = read_file(file_bookmarks)
    post_with_tef = posts_wish_teg(posts)
    return render_template('bookmarks.html', posts=post_with_tef)




