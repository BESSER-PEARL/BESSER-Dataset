





import java.util.List;
import java.util.ArrayList;

public class publication2014a_ReviewNote extends Named {

    private String content;





    private publication2014a_Paragraph publication2014a_paragraph;


    public publication2014a_ReviewNote(
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

    public publication2014a_Paragraph getPublication2014a_paragraph() {
        return publication2014a_paragraph;
    }

    public void setPublication2014a_paragraph(publication2014a_Paragraph publication2014a_paragraph) {
        this.publication2014a_paragraph = publication2014a_paragraph;
    }

}