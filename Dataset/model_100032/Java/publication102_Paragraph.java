





import java.util.List;
import java.util.ArrayList;

public class publication102_Paragraph extends Counted, Named {

    private String content;





    private publication102_Paper publication102_paper;




    private publication102_Write publication102_write;




    private List<publication102_ReviewNote> publication102_reviewnotes;


    public publication102_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.publication102_reviewnotes = new ArrayList<>();
    }

    public publication102_Paragraph(
        String content        ArrayList<publication102_ReviewNote> publication102_reviewnotes    ) {
        this.content = content;
        this.publication102_reviewnotes = publication102_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public publication102_Paper getPublication102_paper() {
        return publication102_paper;
    }

    public void setPublication102_paper(publication102_Paper publication102_paper) {
        this.publication102_paper = publication102_paper;
    }
    public publication102_Write getPublication102_write() {
        return publication102_write;
    }

    public void setPublication102_write(publication102_Write publication102_write) {
        this.publication102_write = publication102_write;
    }
    public List<publication102_ReviewNote> getPublication102_reviewnotes() {
        return publication102_reviewnotes;
    }

    public void addPublication102_reviewnote(Publication102_reviewnote publication102_reviewnote) {
        this.publication102_reviewnotes.add(publication102_reviewnote);
    }

}