





import java.util.List;
import java.util.ArrayList;

public class revision_Paragraph extends Counted, Named {

    private String content;





    private revision_Paper revision_paper;




    private List<revision_ReviewNote> revision_reviewnotes;


    public revision_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.revision_reviewnotes = new ArrayList<>();
    }

    public revision_Paragraph(
        String content        ArrayList<revision_ReviewNote> revision_reviewnotes    ) {
        this.content = content;
        this.revision_reviewnotes = revision_reviewnotes;
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
    public List<revision_ReviewNote> getRevision_reviewnotes() {
        return revision_reviewnotes;
    }

    public void addRevision_reviewnote(Revision_reviewnote revision_reviewnote) {
        this.revision_reviewnotes.add(revision_reviewnote);
    }

}