





import java.util.List;
import java.util.ArrayList;

public class publication103_Paragraph extends Counted, Named {

    private String content;





    private List<publication103_ReviewNote> publication103_reviewnotes;




    private publication103_Write publication103_write;




    private publication103_Paper publication103_paper;


    public publication103_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.publication103_reviewnotes = new ArrayList<>();
    }

    public publication103_Paragraph(
        String content        ArrayList<publication103_ReviewNote> publication103_reviewnotes    ) {
        this.content = content;
        this.publication103_reviewnotes = publication103_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<publication103_ReviewNote> getPublication103_reviewnotes() {
        return publication103_reviewnotes;
    }

    public void addPublication103_reviewnote(Publication103_reviewnote publication103_reviewnote) {
        this.publication103_reviewnotes.add(publication103_reviewnote);
    }
    public publication103_Write getPublication103_write() {
        return publication103_write;
    }

    public void setPublication103_write(publication103_Write publication103_write) {
        this.publication103_write = publication103_write;
    }
    public publication103_Paper getPublication103_paper() {
        return publication103_paper;
    }

    public void setPublication103_paper(publication103_Paper publication103_paper) {
        this.publication103_paper = publication103_paper;
    }

}