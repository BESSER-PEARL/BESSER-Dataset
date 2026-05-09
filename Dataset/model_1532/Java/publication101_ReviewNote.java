





import java.util.List;
import java.util.ArrayList;

public class publication101_ReviewNote extends Named {

    private String content;





    private publication101_Paragraph publication101_paragraph;


    public publication101_ReviewNote(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public publication101_Paragraph getPublication101_paragraph() {
        return publication101_paragraph;
    }

    public void setPublication101_paragraph(publication101_Paragraph publication101_paragraph) {
        this.publication101_paragraph = publication101_paragraph;
    }

}