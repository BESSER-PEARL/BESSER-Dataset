





import java.util.List;
import java.util.ArrayList;

public class revision_ReviewNote extends Named {

    private String content;





    private revision_Paragraph revision_paragraph;


    public revision_ReviewNote(
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

    public revision_Paragraph getRevision_paragraph() {
        return revision_paragraph;
    }

    public void setRevision_paragraph(revision_Paragraph revision_paragraph) {
        this.revision_paragraph = revision_paragraph;
    }

}