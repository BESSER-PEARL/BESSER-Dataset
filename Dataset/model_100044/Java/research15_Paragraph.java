





import java.util.List;
import java.util.ArrayList;

public class research15_Paragraph extends Named, Counted {

    private String content;





    private List<research15_ReviewNote> research15_reviewnotes;


    public research15_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.research15_reviewnotes = new ArrayList<>();
    }

    public research15_Paragraph(
        String content        ArrayList<research15_ReviewNote> research15_reviewnotes    ) {
        this.content = content;
        this.research15_reviewnotes = research15_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<research15_ReviewNote> getResearch15_reviewnotes() {
        return research15_reviewnotes;
    }

    public void addResearch15_reviewnote(Research15_reviewnote research15_reviewnote) {
        this.research15_reviewnotes.add(research15_reviewnote);
    }

}