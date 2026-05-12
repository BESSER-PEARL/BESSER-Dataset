





import java.util.List;
import java.util.ArrayList;

public class research_Paragraph extends Counted, Named {

    private String content;





    private List<research_ReviewNote> research_reviewnotes;




    private research_Write research_write;




    private research_Paper research_paper;


    public research_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.research_reviewnotes = new ArrayList<>();
    }

    public research_Paragraph(
        String content        ArrayList<research_ReviewNote> research_reviewnotes    ) {
        this.content = content;
        this.research_reviewnotes = research_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<research_ReviewNote> getResearch_reviewnotes() {
        return research_reviewnotes;
    }

    public void addResearch_reviewnote(Research_reviewnote research_reviewnote) {
        this.research_reviewnotes.add(research_reviewnote);
    }
    public research_Write getResearch_write() {
        return research_write;
    }

    public void setResearch_write(research_Write research_write) {
        this.research_write = research_write;
    }
    public research_Paper getResearch_paper() {
        return research_paper;
    }

    public void setResearch_paper(research_Paper research_paper) {
        this.research_paper = research_paper;
    }

}