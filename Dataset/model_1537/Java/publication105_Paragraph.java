





import java.util.List;
import java.util.ArrayList;

public class publication105_Paragraph extends Counted, Named {

    private String content;





    private List<publication105_ReviewNote> publication105_reviewnotes;




    private publication105_Paper publication105_paper;


    public publication105_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.publication105_reviewnotes = new ArrayList<>();
    }

    public publication105_Paragraph(
        String content        ArrayList<publication105_ReviewNote> publication105_reviewnotes    ) {
        this.content = content;
        this.publication105_reviewnotes = publication105_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<publication105_ReviewNote> getPublication105_reviewnotes() {
        return publication105_reviewnotes;
    }

    public void addPublication105_reviewnote(Publication105_reviewnote publication105_reviewnote) {
        this.publication105_reviewnotes.add(publication105_reviewnote);
    }
    public publication105_Paper getPublication105_paper() {
        return publication105_paper;
    }

    public void setPublication105_paper(publication105_Paper publication105_paper) {
        this.publication105_paper = publication105_paper;
    }

}