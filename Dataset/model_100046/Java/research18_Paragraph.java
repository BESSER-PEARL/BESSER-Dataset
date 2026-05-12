





import java.util.List;
import java.util.ArrayList;

public class research18_Paragraph extends Named, Counted {

    private String content;





    private List<research18_ReviewNote> research18_reviewnotes;




    private research18_Paper research18_paper;


    public research18_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.research18_reviewnotes = new ArrayList<>();
    }

    public research18_Paragraph(
        String content        ArrayList<research18_ReviewNote> research18_reviewnotes    ) {
        this.content = content;
        this.research18_reviewnotes = research18_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<research18_ReviewNote> getResearch18_reviewnotes() {
        return research18_reviewnotes;
    }

    public void addResearch18_reviewnote(Research18_reviewnote research18_reviewnote) {
        this.research18_reviewnotes.add(research18_reviewnote);
    }
    public research18_Paper getResearch18_paper() {
        return research18_paper;
    }

    public void setResearch18_paper(research18_Paper research18_paper) {
        this.research18_paper = research18_paper;
    }

}