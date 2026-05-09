





import java.util.List;
import java.util.ArrayList;

public class publication2014b_Rule  {

    private String key;
    private String text;





    private publication2014b_PublicationProcess publication2014b_publicationprocess;


    public publication2014b_Rule(
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

    public publication2014b_PublicationProcess getPublication2014b_publicationprocess() {
        return publication2014b_publicationprocess;
    }

    public void setPublication2014b_publicationprocess(publication2014b_PublicationProcess publication2014b_publicationprocess) {
        this.publication2014b_publicationprocess = publication2014b_publicationprocess;
    }

}