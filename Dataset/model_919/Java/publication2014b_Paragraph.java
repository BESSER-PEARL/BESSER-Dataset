





import java.util.List;
import java.util.ArrayList;

public class publication2014b_Paragraph extends Counted, Named {

    private String content;





    private List<publication2014b_ReviewNote> publication2014b_reviewnotes;


    public publication2014b_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.publication2014b_reviewnotes = new ArrayList<>();
    }

    public publication2014b_Paragraph(
        String content        ArrayList<publication2014b_ReviewNote> publication2014b_reviewnotes    ) {
        this.content = content;
        this.publication2014b_reviewnotes = publication2014b_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<publication2014b_ReviewNote> getPublication2014b_reviewnotes() {
        return publication2014b_reviewnotes;
    }

    public void addPublication2014b_reviewnote(Publication2014b_reviewnote publication2014b_reviewnote) {
        this.publication2014b_reviewnotes.add(publication2014b_reviewnote);
    }

}