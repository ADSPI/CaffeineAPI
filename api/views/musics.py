from rest_framework.generics import GenericAPIView

from api.appresponse import AppResponse
from api.models import Music
from api.serializers.music import MusicSerializer


class MusicsView(GenericAPIView):
    @staticmethod
    def get(request):

        try:
            carrousel_cards = []
            cards = []

            musics_qs = Music.objects.all().order_by('?')[:12]

            music_count = 1
            musics_s = MusicSerializer(musics_qs, many=True)
            musics = musics_s.data


            for music in musics:
                cards.append(music)
                music_count += 1
                if music_count > 4:
                    carrousel_cards.append(cards)
                    music_count = 1
                    cards = []

            return AppResponse.get_success(data=carrousel_cards)
        except Exception as e:
            return AppResponse.get_error(reason=str(e))
