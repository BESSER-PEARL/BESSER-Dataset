





import java.util.List;
import java.util.ArrayList;

public class album  {

    private None publisher;
    private String genre;
    private String title;
    private String duration;
    private None rightsReserve;
    private String price;
    private String publishDate;
    private String albumID;
    private String cover;
    private None artists;



    public album(
        None publisher,        String genre,        String title,        String duration,        None rightsReserve,        String price,        String publishDate,        String albumID,        String cover,        None artists    ) {
        this.publisher = publisher;
        this.genre = genre;
        this.title = title;
        this.duration = duration;
        this.rightsReserve = rightsReserve;
        this.price = price;
        this.publishDate = publishDate;
        this.albumID = albumID;
        this.cover = cover;
        this.artists = artists;
    }


    public None getPublisher() {
        return publisher;
    }

    public void setPublisher(None publisher) {
        this.publisher = publisher;
    }
    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public None getRightsreserve() {
        return rightsReserve;
    }

    public void setRightsreserve(None rightsReserve) {
        this.rightsReserve = rightsReserve;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getPublishdate() {
        return publishDate;
    }

    public void setPublishdate(String publishDate) {
        this.publishDate = publishDate;
    }
    public String getAlbumid() {
        return albumID;
    }

    public void setAlbumid(String albumID) {
        this.albumID = albumID;
    }
    public String getCover() {
        return cover;
    }

    public void setCover(String cover) {
        this.cover = cover;
    }
    public None getArtists() {
        return artists;
    }

    public void setArtists(None artists) {
        this.artists = artists;
    }


}