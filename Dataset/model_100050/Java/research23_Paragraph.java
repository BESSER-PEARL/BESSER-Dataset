





import java.util.List;
import java.util.ArrayList;

public class research23_Paragraph extends Counted, Named {

    private String content;





    private research23_Paper research23_paper;




    private List<research23_ReviewNote> research23_reviewnotes;


    public research23_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.research23_reviewnotes = new ArrayList<>();
    }

    public research23_Paragraph(
        String content        ArrayList<research23_ReviewNote> research23_reviewnotes    ) {
        this.content = content;
        this.research23_reviewnotes = research23_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public research23_Paper getResearch23_paper() {
        return research23_paper;
    }

    public void setResearch23_paper(research23_Paper research23_paper) {
        this.research23_paper = research23_paper;
    }
    public List<research23_ReviewNote> getResearch23_reviewnotes() {
        return research23_reviewnotes;
    }

    public void addResearch23_reviewnote(Research23_reviewnote research23_reviewnote) {
        this.research23_reviewnotes.add(research23_reviewnote);
    }

}