





import java.util.List;
import java.util.ArrayList;

public class research13_Paragraph extends Named, Counted {

    private String content;





    private research13_Write research13_write;




    private research13_Paper research13_paper;




    private List<research13_ReviewNote> research13_reviewnotes;


    public research13_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.research13_reviewnotes = new ArrayList<>();
    }

    public research13_Paragraph(
        String content        ArrayList<research13_ReviewNote> research13_reviewnotes    ) {
        this.content = content;
        this.research13_reviewnotes = research13_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public research13_Write getResearch13_write() {
        return research13_write;
    }

    public void setResearch13_write(research13_Write research13_write) {
        this.research13_write = research13_write;
    }
    public research13_Paper getResearch13_paper() {
        return research13_paper;
    }

    public void setResearch13_paper(research13_Paper research13_paper) {
        this.research13_paper = research13_paper;
    }
    public List<research13_ReviewNote> getResearch13_reviewnotes() {
        return research13_reviewnotes;
    }

    public void addResearch13_reviewnote(Research13_reviewnote research13_reviewnote) {
        this.research13_reviewnotes.add(research13_reviewnote);
    }

}