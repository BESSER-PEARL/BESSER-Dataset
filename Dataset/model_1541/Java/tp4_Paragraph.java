





import java.util.List;
import java.util.ArrayList;

public class tp4_Paragraph extends Named, Counted {

    private String content;





    private List<tp4_ReviewNote> tp4_reviewnotes;


    public tp4_Paragraph(
        String content    ) {
        super(
        );
        this.content = content;
        this.tp4_reviewnotes = new ArrayList<>();
    }

    public tp4_Paragraph(
        String content        ArrayList<tp4_ReviewNote> tp4_reviewnotes    ) {
        this.content = content;
        this.tp4_reviewnotes = tp4_reviewnotes;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<tp4_ReviewNote> getTp4_reviewnotes() {
        return tp4_reviewnotes;
    }

    public void addTp4_reviewnote(Tp4_reviewnote tp4_reviewnote) {
        this.tp4_reviewnotes.add(tp4_reviewnote);
    }

}