





import java.util.List;
import java.util.ArrayList;

public class song  {

    private None artistLyrics;
    private None artistCompose;
    private None belongsTo;
    private None artistVocal;
    private String title;
    private int year;
    private String genre;
    private String price;
    private None artistPerform;
    private None rightsReserve;
    private int trackID;
    private String cover;
    private String songID;
    private String duration;



    public song(
        None artistLyrics,        None artistCompose,        None belongsTo,        None artistVocal,        String title,        int year,        String genre,        String price,        None artistPerform,        None rightsReserve,        int trackID,        String cover,        String songID,        String duration    ) {
        this.artistLyrics = artistLyrics;
        this.artistCompose = artistCompose;
        this.belongsTo = belongsTo;
        this.artistVocal = artistVocal;
        this.title = title;
        this.year = year;
        this.genre = genre;
        this.price = price;
        this.artistPerform = artistPerform;
        this.rightsReserve = rightsReserve;
        this.trackID = trackID;
        this.cover = cover;
        this.songID = songID;
        this.duration = duration;
    }


    public None getArtistlyrics() {
        return artistLyrics;
    }

    public void setArtistlyrics(None artistLyrics) {
        this.artistLyrics = artistLyrics;
    }
    public None getArtistcompose() {
        return artistCompose;
    }

    public void setArtistcompose(None artistCompose) {
        this.artistCompose = artistCompose;
    }
    public None getBelongsto() {
        return belongsTo;
    }

    public void setBelongsto(None belongsTo) {
        this.belongsTo = belongsTo;
    }
    public None getArtistvocal() {
        return artistVocal;
    }

    public void setArtistvocal(None artistVocal) {
        this.artistVocal = artistVocal;
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
    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public None getArtistperform() {
        return artistPerform;
    }

    public void setArtistperform(None artistPerform) {
        this.artistPerform = artistPerform;
    }
    public None getRightsreserve() {
        return rightsReserve;
    }

    public void setRightsreserve(None rightsReserve) {
        this.rightsReserve = rightsReserve;
    }
    public int getTrackid() {
        return trackID;
    }

    public void setTrackid(int trackID) {
        this.trackID = trackID;
    }
    public String getCover() {
        return cover;
    }

    public void setCover(String cover) {
        this.cover = cover;
    }
    public String getSongid() {
        return songID;
    }

    public void setSongid(String songID) {
        this.songID = songID;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }


}