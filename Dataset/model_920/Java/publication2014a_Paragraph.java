





import java.util.List;
import java.util.ArrayList;

public class publication2014a_Paragraph extends Counted, Named {

    private String content;





    private List<publication2014a_ReviewNote> publication2014a_reviewnotes;




    private publication2014a_Paper publication2014a_paper;


    public publication2014a_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.publication2014a_reviewnotes = new ArrayList<>();
    }

    public publication2014a_Paragraph(
        String content        ArrayList<publication2014a_ReviewNote> publication2014a_reviewnotes    ) {
        this.content = content;
        this.publication2014a_reviewnotes = publication2014a_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<publication2014a_ReviewNote> getPublication2014a_reviewnotes() {
        return publication2014a_reviewnotes;
    }

    public void addPublication2014a_reviewnote(Publication2014a_reviewnote publication2014a_reviewnote) {
        this.publication2014a_reviewnotes.add(publication2014a_reviewnote);
    }
    public publication2014a_Paper getPublication2014a_paper() {
        return publication2014a_paper;
    }

    public void setPublication2014a_paper(publication2014a_Paper publication2014a_paper) {
        this.publication2014a_paper = publication2014a_paper;
    }

}