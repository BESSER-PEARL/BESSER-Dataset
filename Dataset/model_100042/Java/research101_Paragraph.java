





import java.util.List;
import java.util.ArrayList;

public class research101_Paragraph extends Counted, Named {

    private String content;





    private List<research101_ReviewNote> research101_reviewnotes;


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

    public List<research101_ReviewNote> getResearch101_reviewnotes() {
        return research101_reviewnotes;
    }

    public void addResearch101_reviewnote(Research101_reviewnote research101_reviewnote) {
        this.research101_reviewnotes.add(research101_reviewnote);
    }

}