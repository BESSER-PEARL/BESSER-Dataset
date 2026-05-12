





import java.util.List;
import java.util.ArrayList;

public class publication101_Phase  {

    private String name;





    private publication101_PublicationProcess publication101_publicationprocess;


    public publication101_Phase(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public publication101_PublicationProcess getPublication101_publicationprocess() {
        return publication101_publicationprocess;
    }

    public void setPublication101_publicationprocess(publication101_PublicationProcess publication101_publicationprocess) {
        this.publication101_publicationprocess = publication101_publicationprocess;
    }

}