





import java.util.List;
import java.util.ArrayList;

public class music_Work  {

    private String notes;
    private String mediaTypes;
    private String name;
    private String whenMade;





    private music_Artist music_artist;




    private music_Artist music_artist;


    public music_Work(
        String notes,        String mediaTypes,        String name,        String whenMade    ) {
        this.notes = notes;
        this.mediaTypes = mediaTypes;
        this.name = name;
        this.whenMade = whenMade;
    }


    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public String getMediatypes() {
        return mediaTypes;
    }

    public void setMediatypes(String mediaTypes) {
        this.mediaTypes = mediaTypes;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWhenmade() {
        return whenMade;
    }

    public void setWhenmade(String whenMade) {
        this.whenMade = whenMade;
    }

    public music_Artist getMusic_artist() {
        return music_artist;
    }

    public void setMusic_artist(music_Artist music_artist) {
        this.music_artist = music_artist;
    }
    public music_Artist getMusic_artist() {
        return music_artist;
    }

    public void setMusic_artist(music_Artist music_artist) {
        this.music_artist = music_artist;
    }

}