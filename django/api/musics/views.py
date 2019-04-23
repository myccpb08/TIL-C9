from django.shortcuts import render, get_object_or_404
from .models import Music, Artist, Comment
from rest_framework.decorators import api_view
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
from rest_framework.response import Response


# api 는 일반적 페이지와 요청하는 것부터 다르고, return 도 다름 (render, redirect 안 씀)
# 들어오는 요청을 filtering 해주는 애가 있음

@api_view(['GET'])  # 어떤 요청만 허용할 것인지
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)  # musics 에 노래가 '여러개' 들어있다고 알려줘야 함
    # Serializer : object 로 꽁꽁 뭉쳐져있는 것으로부터 필요한 것만 뽑아서 문자열로 만들어주는 역할을 하는 아이. ≒ 번역기
    return Response(serializer.data)  # 요청이 들어왔으면 항상 응답(response 객체로)으로 return 해야한다
    
@api_view(['GET'])
def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    serializer = MusicSerializer(music)
    return Response(serializer.data)
    
@api_view(['GET'])  # 어떤 요청만 허용할 것인지
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)
    
@api_view(['POST'])  # form 처럼 쓰면 된다
def comment_create(request, music_id):
    serializer = CommentSerializer(data=request.data)  # 음악에 대한 정보없이 댓글 콘텐츠만 넘어와서 댓글을 만들었음. 아직 저장은 x
    if serializer.is_valid(raise_exception=True):  # 폼처럼사용하되, 유효하지 않은 값이 들어왔을 때 404에러 응답을 보여주기 위하여, raise_Exception 필요함
                                                   # 없으면, 이 줄 코드자체에서 에러가 나버림
                                                   # 넘어온 정보에는 어떤 음악인지 없다. (∵CommentSerializer 의 필드는 id와  content)                                                  # 하지만 valid 는 통과하는데, db에 저장할 때는 노래를 반영해야함
        serializer.save(music_id=music_id)  # 여기서 어떤 노래의 댓글인지 반영
    return Response(serializer.data)
    
@api_view(['PUT', 'DELETE'])  # PUT : 수정할 때, delete: 삭제할 때    
def comment_update_and_delete(request, music_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)  # 수정 또는 삭제할 댓글 가져오기
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)  # instance=comment 부분이 create 랑 다름
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Comment has been updated!'})
            
    else:   # 삭제요청이 들어왔다면
        comment.delete()
        return Response({'message': 'Comment has been deleted!'})
    