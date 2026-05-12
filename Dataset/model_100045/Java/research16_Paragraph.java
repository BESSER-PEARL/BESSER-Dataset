





import java.util.List;
import java.util.ArrayList;

public class research16_Paragraph extends Named, Counted {

    private String content;





    private List<research16_ReviewNote> research16_reviewnotes;




    private research16_Write research16_write;




    private research16_Paper research16_paper;


    public research16_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.research16_reviewnotes = new ArrayList<>();
    }

    public research16_Paragraph(
        String content        ArrayList<research16_ReviewNote> research16_reviewnotes    ) {
        this.content = content;
        this.research16_reviewnotes = research16_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<research16_ReviewNote> getResearch16_reviewnotes() {
        return research16_reviewnotes;
    }

    public void addResearch16_reviewnote(Research16_reviewnote research16_reviewnote) {
        this.research16_reviewnotes.add(research16_reviewnote);
    }
    public research16_Write getResearch16_write() {
        return research16_write;
    }

    public void setResearch16_write(research16_Write research16_write) {
        this.research16_write = research16_write;
    }
    public research16_Paper getResearch16_paper() {
        return research16_paper;
    }

    public void setResearch16_paper(research16_Paper research16_paper) {
        this.research16_paper = research16_paper;
    }

}