





import java.util.List;
import java.util.ArrayList;

public class revision_Rule  {

    private String key;
    private String text;





    private revision_PublicationPhase revision_publicationphase;




    private revision_PublicationProcess revision_publicationprocess;


    public revision_Rule(
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

    public revision_PublicationPhase getRevision_publicationphase() {
        return revision_publicationphase;
    }

    public void setRevision_publicationphase(revision_PublicationPhase revision_publicationphase) {
        this.revision_publicationphase = revision_publicationphase;
    }
    public revision_PublicationProcess getRevision_publicationprocess() {
        return revision_publicationprocess;
    }

    public void setRevision_publicationprocess(revision_PublicationProcess revision_publicationprocess) {
        this.revision_publicationprocess = revision_publicationprocess;
    }

}