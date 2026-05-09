





import java.util.List;
import java.util.ArrayList;

public class extlibraryprofile_Item  {

    private String publicationDate;
    private String title;



    public extlibraryprofile_Item(
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


}