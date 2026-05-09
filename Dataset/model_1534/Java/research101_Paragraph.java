





import java.util.List;
import java.util.ArrayList;

public class research101_Paragraph extends Counted, Named {

    private String content;





    private research101_Write research101_write;




    private List<research101_ReviewNote> research101_reviewnotes;




    private research101_Paper research101_paper;


    public research101_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.research101_reviewnotes = new ArrayList<>();
    }

    public research101_Paragraph(
        String content        ArrayList<research101_ReviewNote> research101_reviewnotes    ) {
        this.content = content;
        this.research101_reviewnotes = research101_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public research101_Write getResearch101_write() {
        return research101_write;
    }

    public void setResearch101_write(research101_Write research101_write) {
        this.research101_write = research101_write;
    }
    public List<research101_ReviewNote> getResearch101_reviewnotes() {
        return research101_reviewnotes;
    }

    public void addResearch101_reviewnote(Research101_reviewnote research101_reviewnote) {
        this.research101_reviewnotes.add(research101_reviewnote);
    }
    public research101_Paper getResearch101_paper() {
        return research101_paper;
    }

    public void setResearch101_paper(research101_Paper research101_paper) {
        this.research101_paper = research101_paper;
    }

}