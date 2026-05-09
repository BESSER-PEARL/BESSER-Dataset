





import java.util.List;
import java.util.ArrayList;

public class music_MusicLibrary  {

    private String name;





    private List<music_Artist> music_artists;


    public music_MusicLibrary(
        String name    ) {
        this.name = name;
        this.music_artists = new ArrayList<>();
    }

    public music_MusicLibrary(
        String name        ArrayList<music_Artist> music_artists    ) {
        this.name = name;
        this.music_artists = music_artists;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<music_Artist> getMusic_artists() {
        return music_artists;
    }

    public void addMusic_artist(Music_artist music_artist) {
        this.music_artists.add(music_artist);
    }

}