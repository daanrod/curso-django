from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'youtube_id': '2aYplgJrPDU'},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'youtube_id': 'hQayuyeEMy0'}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
