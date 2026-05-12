





import java.util.List;
import java.util.ArrayList;

public class publication2014a_Rule  {

    private String text;
    private String key;





    private publication2014a_PublicationPhase publication2014a_publicationphase;




    private publication2014a_PublicationProcess publication2014a_publicationprocess;


    public publication2014a_Rule(
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

    public publication2014a_PublicationPhase getPublication2014a_publicationphase() {
        return publication2014a_publicationphase;
    }

    public void setPublication2014a_publicationphase(publication2014a_PublicationPhase publication2014a_publicationphase) {
        this.publication2014a_publicationphase = publication2014a_publicationphase;
    }
    public publication2014a_PublicationProcess getPublication2014a_publicationprocess() {
        return publication2014a_publicationprocess;
    }

    public void setPublication2014a_publicationprocess(publication2014a_PublicationProcess publication2014a_publicationprocess) {
        this.publication2014a_publicationprocess = publication2014a_publicationprocess;
    }

}