





import java.util.List;
import java.util.ArrayList;

public class research2_Paragraph extends Named, Counted {

    private String content;





    private research2_Paper research2_paper;




    private research2_Write research2_write;




    private List<research2_ReviewNote> research2_reviewnotes;


    public research2_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.research2_reviewnotes = new ArrayList<>();
    }

    public research2_Paragraph(
        String content        ArrayList<research2_ReviewNote> research2_reviewnotes    ) {
        this.content = content;
        this.research2_reviewnotes = research2_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public research2_Paper getResearch2_paper() {
        return research2_paper;
    }

    public void setResearch2_paper(research2_Paper research2_paper) {
        this.research2_paper = research2_paper;
    }
    public research2_Write getResearch2_write() {
        return research2_write;
    }

    public void setResearch2_write(research2_Write research2_write) {
        this.research2_write = research2_write;
    }
    public List<research2_ReviewNote> getResearch2_reviewnotes() {
        return research2_reviewnotes;
    }

    public void addResearch2_reviewnote(Research2_reviewnote research2_reviewnote) {
        this.research2_reviewnotes.add(research2_reviewnote);
    }

}