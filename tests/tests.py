#import pytest

from utils import posts_wish_teg

posts = [[{'content': '������ � ��� ����� #���� #������� �� #pyton'}],
         [{'content': '������ � ��� ����� #���� #������� �� #pyton', 'teg_words': ['����', '�������', 'pyton']}]]

print(posts_wish_teg([{'content': '������ � ��� ����� #���� #������� �� #pyton'}]))

# @pytest.mark.parametrize("post, post_with_teg", posts)
# def test_posts_wish_teg(post, post_with_teg):
#     assert posts_wish_teg(post) == post_with_teg
