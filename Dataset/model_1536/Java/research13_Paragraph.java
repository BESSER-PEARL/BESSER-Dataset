





import java.util.List;
import java.util.ArrayList;

public class research13_Paragraph extends Counted, Named {

    private String content;





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

    public List<research13_ReviewNote> getResearch13_reviewnotes() {
        return research13_reviewnotes;
    }

    public void addResearch13_reviewnote(Research13_reviewnote research13_reviewnote) {
        this.research13_reviewnotes.add(research13_reviewnote);
    }

}