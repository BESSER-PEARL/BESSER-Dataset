





import java.util.List;
import java.util.ArrayList;

public class comicBookCollection2_Book  {

    private String name;
    private String publicationDate;





    private comicBookCollection2_ComicBookCollection comicbookcollection2_comicbookcollection;


    public comicBookCollection2_Book(
        String name,        String publicationDate    ) {
        this.name = name;
        this.publicationDate = publicationDate;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPublicationdate() {
        return publicationDate;
    }

    public void setPublicationdate(String publicationDate) {
        this.publicationDate = publicationDate;
    }

    public comicBookCollection2_ComicBookCollection getComicbookcollection2_comicbookcollection() {
        return comicbookcollection2_comicbookcollection;
    }

    public void setComicbookcollection2_comicbookcollection(comicBookCollection2_ComicBookCollection comicbookcollection2_comicbookcollection) {
        this.comicbookcollection2_comicbookcollection = comicbookcollection2_comicbookcollection;
    }

}