





import java.util.List;
import java.util.ArrayList;

public class publication_ReviewNote extends Named {

    private String content;





    private publication_Paragraph publication_paragraph;


    public publication_ReviewNote(
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

    public publication_Paragraph getPublication_paragraph() {
        return publication_paragraph;
    }

    public void setPublication_paragraph(publication_Paragraph publication_paragraph) {
        this.publication_paragraph = publication_paragraph;
    }

}