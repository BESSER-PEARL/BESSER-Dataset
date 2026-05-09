





import java.util.List;
import java.util.ArrayList;

public class publication2014c_Rule  {

    private String key;
    private String text;





    private publication2014c_PublicationProcess publication2014c_publicationprocess;




    private publication2014c_PublicationPhase publication2014c_publicationphase;


    public publication2014c_Rule(
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

    public publication2014c_PublicationProcess getPublication2014c_publicationprocess() {
        return publication2014c_publicationprocess;
    }

    public void setPublication2014c_publicationprocess(publication2014c_PublicationProcess publication2014c_publicationprocess) {
        this.publication2014c_publicationprocess = publication2014c_publicationprocess;
    }
    public publication2014c_PublicationPhase getPublication2014c_publicationphase() {
        return publication2014c_publicationphase;
    }

    public void setPublication2014c_publicationphase(publication2014c_PublicationPhase publication2014c_publicationphase) {
        this.publication2014c_publicationphase = publication2014c_publicationphase;
    }

}