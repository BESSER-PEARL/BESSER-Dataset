





import java.util.List;
import java.util.ArrayList;

public class publication2014_Rule  {

    private String key;
    private String text;





    private publication2014_PublicationPhase publication2014_publicationphase;




    private publication2014_PublicationProcess publication2014_publicationprocess;


    public publication2014_Rule(
        String key,        String text    ) {
        this.key = key;
        this.text = text;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public publication2014_PublicationPhase getPublication2014_publicationphase() {
        return publication2014_publicationphase;
    }

    public void setPublication2014_publicationphase(publication2014_PublicationPhase publication2014_publicationphase) {
        this.publication2014_publicationphase = publication2014_publicationphase;
    }
    public publication2014_PublicationProcess getPublication2014_publicationprocess() {
        return publication2014_publicationprocess;
    }

    public void setPublication2014_publicationprocess(publication2014_PublicationProcess publication2014_publicationprocess) {
        this.publication2014_publicationprocess = publication2014_publicationprocess;
    }

}