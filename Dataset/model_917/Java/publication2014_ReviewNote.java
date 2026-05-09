





import java.util.List;
import java.util.ArrayList;

public class publication2014_ReviewNote extends Named {

    private String content;





    private publication2014_Paragraph publication2014_paragraph;


    public publication2014_ReviewNote(
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

    public publication2014_Paragraph getPublication2014_paragraph() {
        return publication2014_paragraph;
    }

    public void setPublication2014_paragraph(publication2014_Paragraph publication2014_paragraph) {
        this.publication2014_paragraph = publication2014_paragraph;
    }

}