





import java.util.List;
import java.util.ArrayList;

public class publication103_ReviewNote extends Named {

    private String content;





    private publication103_Paragraph publication103_paragraph;


    public publication103_ReviewNote(
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

    public publication103_Paragraph getPublication103_paragraph() {
        return publication103_paragraph;
    }

    public void setPublication103_paragraph(publication103_Paragraph publication103_paragraph) {
        this.publication103_paragraph = publication103_paragraph;
    }

}