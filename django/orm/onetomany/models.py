from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()  # 글쓴이의 이름을 담는 column
    
# User : Post = 1: N
# ForeignKey : 참조되는 릴레이션의 '기본키'와 대응되어 릴레이션 간에 참조 관계를 표현
class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 이 글을 누가 썼는지 그 사람의 id를 저장?  ex) post.user = 그 사람의 id 
    # USER 라는 COLUMN 에 1이라는 ID 가 저장되어 있음? 
    # 그냥 글쓴이의 이름만 가져오면, user 에는 다양한 정보가 있지만 이름밖에 못 가져옴.
    # 그래서 foreignkey 로 그냥 관계를 만들어 놓으면 다양한 정보를 가져올 수 있음? ㅜㅜㅜㅜ
    
# User : Comment = 1: N
# Post : Comment = 1: N
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 어떤 유저가 쓴 댓글이냐   물건에 이름을 적어야 누군지 아는 것처럼, 댓글(N쪽) 에 이름(user)을 써야 됨
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 어떤 게시글에 대한 댓글이냐
    
    
# 예시
# 1. 1번 사람이 작성한 게시글은?
# >> user1.post_set.all()    user1= 1번사람이, post_set 작성한, all() 모든 글

# 2. 1번 사람이 작성한 게시글의 댓글 내용을 출력
# >> user1.post_set.all()  이 리스트 형식이므로, 각 글에 대한 반복문이 필요하다
# >>> for post in user1.post_set.all():  # 1번 사람이 작성한 글에 대하여
# ...     for comment in post.comment_set.all():  # 그 글에 달린 모든 댓글 (다른 사람이 쓴 댓글도)
# ...             print(comment.content)   # 출력하라

# 3. c2 를 누가 썼는지
# c2.user

# 4. c2 를 쓴 사람이 쓴 글은?
# >>> c2.user.post_set.all()
# <QuerySet [<Post: Post object (3)>]>

# 5. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
# post1.comment_set.all()[0].user.name  또는
# post1.comment_set.first().user.name


# 6. '1글' 이 제목인 게시글은?
# >>> Post.objects.filter(title='1글')

# 7. 댓글 중에 해당 게시글의 제목이 1글인 것은?
# 방법 1
# >>> Comment.objects.filter(post__title='1글')
# 방법 2
# >>> post1 = Post.objects.get(title='1글')
# >>> Comment.objects.filter(post=post1)

# 8. 댓글 중에 해당 게시글의 제목에 '1'이 들어가 있는 것은?
# Comment.objects.filter(post__title__contains='1')