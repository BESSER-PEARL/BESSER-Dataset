





import java.util.List;
import java.util.ArrayList;

public class publication_Rule  {

    private String text;
    private String key;





    private publication_PublicationPhase publication_publicationphase;




    private publication_PublicationProcess publication_publicationprocess;


    public publication_Rule(
        String text,        String key    ) {
        this.text = text;
        this.key = key;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public publication_PublicationPhase getPublication_publicationphase() {
        return publication_publicationphase;
    }

    public void setPublication_publicationphase(publication_PublicationPhase publication_publicationphase) {
        this.publication_publicationphase = publication_publicationphase;
    }
    public publication_PublicationProcess getPublication_publicationprocess() {
        return publication_publicationprocess;
    }

    public void setPublication_publicationprocess(publication_PublicationProcess publication_publicationprocess) {
        this.publication_publicationprocess = publication_publicationprocess;
    }

}