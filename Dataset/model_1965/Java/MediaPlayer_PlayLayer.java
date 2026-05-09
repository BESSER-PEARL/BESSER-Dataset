





import java.util.List;
import java.util.ArrayList;

public class MediaPlayer_PlayLayer  {






    private List<MediaPlayer_MediaApi> mediaplayer_mediaapis;




    private MediaPlayer_Library mediaplayer_library;


    public MediaPlayer_PlayLayer(
    ) {
        this.mediaplayer_mediaapis = new ArrayList<>();
    }

    public MediaPlayer_PlayLayer(
        ArrayList<MediaPlayer_MediaApi> mediaplayer_mediaapis    ) {
        this.mediaplayer_mediaapis = mediaplayer_mediaapis;
    }


    public List<MediaPlayer_MediaApi> getMediaplayer_mediaapis() {
        return mediaplayer_mediaapis;
    }

    public void addMediaplayer_mediaapi(Mediaplayer_mediaapi mediaplayer_mediaapi) {
        this.mediaplayer_mediaapis.add(mediaplayer_mediaapi);
    }
    public MediaPlayer_Library getMediaplayer_library() {
        return mediaplayer_library;
    }

    public void setMediaplayer_library(MediaPlayer_Library mediaplayer_library) {
        this.mediaplayer_library = mediaplayer_library;
    }

}