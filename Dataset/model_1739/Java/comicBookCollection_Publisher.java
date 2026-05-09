





import java.util.List;
import java.util.ArrayList;

public class comicBookCollection_Publisher  {

    private String publishingName;





    private List<comicBookCollection_Series> comicbookcollection_seriess;




    private comicBookCollection_ComicBookCollection comicbookcollection_comicbookcollection;


    public comicBookCollection_Publisher(
        String publishingName    ) {
        this.publishingName = publishingName;
        this.comicbookcollection_seriess = new ArrayList<>();
    }

    public comicBookCollection_Publisher(
        String publishingName        ArrayList<comicBookCollection_Series> comicbookcollection_seriess    ) {
        this.publishingName = publishingName;
        this.comicbookcollection_seriess = comicbookcollection_seriess;
    }

    public String getPublishingname() {
        return publishingName;
    }

    public void setPublishingname(String publishingName) {
        this.publishingName = publishingName;
    }

    public List<comicBookCollection_Series> getComicbookcollection_seriess() {
        return comicbookcollection_seriess;
    }

    public void addComicbookcollection_series(Comicbookcollection_series comicbookcollection_series) {
        this.comicbookcollection_seriess.add(comicbookcollection_series);
    }
    public comicBookCollection_ComicBookCollection getComicbookcollection_comicbookcollection() {
        return comicbookcollection_comicbookcollection;
    }

    public void setComicbookcollection_comicbookcollection(comicBookCollection_ComicBookCollection comicbookcollection_comicbookcollection) {
        this.comicbookcollection_comicbookcollection = comicbookcollection_comicbookcollection;
    }

}