





import java.util.List;
import java.util.ArrayList;

public class comicBookCollection_Book  {

    private String publicationDate;
    private String title;





    private comicBookCollection_Series comicbookcollection_series;


    public comicBookCollection_Book(
        String publicationDate,        String title    ) {
        this.publicationDate = publicationDate;
        this.title = title;
    }


    public String getPublicationdate() {
        return publicationDate;
    }

    public void setPublicationdate(String publicationDate) {
        this.publicationDate = publicationDate;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public comicBookCollection_Series getComicbookcollection_series() {
        return comicbookcollection_series;
    }

    public void setComicbookcollection_series(comicBookCollection_Series comicbookcollection_series) {
        this.comicbookcollection_series = comicbookcollection_series;
    }

}