





import java.util.List;
import java.util.ArrayList;

public class publication101_Paragraph extends Counted, Named {

    private String content;





    private List<publication101_ReviewNote> publication101_reviewnotes;


    public publication101_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.publication101_reviewnotes = new ArrayList<>();
    }

    public publication101_Paragraph(
        String content        ArrayList<publication101_ReviewNote> publication101_reviewnotes    ) {
        this.content = content;
        this.publication101_reviewnotes = publication101_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<publication101_ReviewNote> getPublication101_reviewnotes() {
        return publication101_reviewnotes;
    }

    public void addPublication101_reviewnote(Publication101_reviewnote publication101_reviewnote) {
        this.publication101_reviewnotes.add(publication101_reviewnote);
    }

}