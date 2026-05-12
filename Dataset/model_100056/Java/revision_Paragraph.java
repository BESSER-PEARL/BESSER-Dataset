





import java.util.List;
import java.util.ArrayList;

public class revision_Paragraph extends Named, Counted {

    private String content;





    private revision_Paper revision_paper;


    public revision_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public revision_Paper getRevision_paper() {
        return revision_paper;
    }

    public void setRevision_paper(revision_Paper revision_paper) {
        this.revision_paper = revision_paper;
    }

}