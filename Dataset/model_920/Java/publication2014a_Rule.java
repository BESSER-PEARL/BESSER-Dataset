





import java.util.List;
import java.util.ArrayList;

public class publication2014a_Rule  {

    private String key;
    private String text;





    private publication2014a_PublicationPhase publication2014a_publicationphase;


    public publication2014a_Rule(
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

    public publication2014a_PublicationPhase getPublication2014a_publicationphase() {
        return publication2014a_publicationphase;
    }

    public void setPublication2014a_publicationphase(publication2014a_PublicationPhase publication2014a_publicationphase) {
        this.publication2014a_publicationphase = publication2014a_publicationphase;
    }

}