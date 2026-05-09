





import java.util.List;
import java.util.ArrayList;

public class MediaPlayer_MediaObject extends BaseObject {

    private String artist;
    private String album;
    private String title;
    private int year;
    private String state;
    private String location;





    private MediaPlayer_Library mediaplayer_library;




    private MediaPlayer_Playlist mediaplayer_playlist;




    private MediaPlayer_MediaApi mediaplayer_mediaapi;




    private MediaPlayer_MediaApi mediaplayer_mediaapi;


    public MediaPlayer_MediaObject(
        String artist,        String album,        String title,        int year,        String state,        String location    ) {
        super(
        );
        this.artist = artist;
        this.album = album;
        this.title = title;
        this.year = year;
        this.state = state;
        this.location = location;
    }


    public String getArtist() {
        return artist;
    }

    public void setArtist(String artist) {
        this.artist = artist;
    }
    public String getAlbum() {
        return album;
    }

    public void setAlbum(String album) {
        this.album = album;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public MediaPlayer_Library getMediaplayer_library() {
        return mediaplayer_library;
    }

    public void setMediaplayer_library(MediaPlayer_Library mediaplayer_library) {
        this.mediaplayer_library = mediaplayer_library;
    }
    public MediaPlayer_Playlist getMediaplayer_playlist() {
        return mediaplayer_playlist;
    }

    public void setMediaplayer_playlist(MediaPlayer_Playlist mediaplayer_playlist) {
        this.mediaplayer_playlist = mediaplayer_playlist;
    }
    public MediaPlayer_MediaApi getMediaplayer_mediaapi() {
        return mediaplayer_mediaapi;
    }

    public void setMediaplayer_mediaapi(MediaPlayer_MediaApi mediaplayer_mediaapi) {
        this.mediaplayer_mediaapi = mediaplayer_mediaapi;
    }
    public MediaPlayer_MediaApi getMediaplayer_mediaapi() {
        return mediaplayer_mediaapi;
    }

    public void setMediaplayer_mediaapi(MediaPlayer_MediaApi mediaplayer_mediaapi) {
        this.mediaplayer_mediaapi = mediaplayer_mediaapi;
    }

}