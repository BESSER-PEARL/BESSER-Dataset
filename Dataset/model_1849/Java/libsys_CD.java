





import java.util.List;
import java.util.ArrayList;

public class libsys_CD extends Medium {

    private String tracks;
    private String genres;
    private String artists;



    public libsys_CD(
        String tracks,        String genres,        String artists    ) {
        super(
        );
        this.tracks = tracks;
        this.genres = genres;
        this.artists = artists;
    }


    public String getTracks() {
        return tracks;
    }

    public void setTracks(String tracks) {
        this.tracks = tracks;
    }
    public String getGenres() {
        return genres;
    }

    public void setGenres(String genres) {
        this.genres = genres;
    }
    public String getArtists() {
        return artists;
    }

    public void setArtists(String artists) {
        this.artists = artists;
    }


}