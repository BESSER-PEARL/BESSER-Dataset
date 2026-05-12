





import java.util.List;
import java.util.ArrayList;

public class revision_Progress extends Labelled {

    private int percent;





    private revision_PublicationProcess revision_publicationprocess;




    private revision_Paper revision_paper;




    private revision_Paper revision_paper;


    public revision_Progress(
        int percent    ) {
        super(
        );
        this.percent = percent;
    }


    public int getPercent() {
        return percent;
    }

    public void setPercent(int percent) {
        this.percent = percent;
    }

    public revision_PublicationProcess getRevision_publicationprocess() {
        return revision_publicationprocess;
    }

    public void setRevision_publicationprocess(revision_PublicationProcess revision_publicationprocess) {
        this.revision_publicationprocess = revision_publicationprocess;
    }
    public revision_Paper getRevision_paper() {
        return revision_paper;
    }

    public void setRevision_paper(revision_Paper revision_paper) {
        this.revision_paper = revision_paper;
    }
    public revision_Paper getRevision_paper() {
        return revision_paper;
    }

    public void setRevision_paper(revision_Paper revision_paper) {
        this.revision_paper = revision_paper;
    }

}