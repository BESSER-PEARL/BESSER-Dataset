





import java.util.List;
import java.util.ArrayList;

public class publication2014c_ReviewNote extends Named {

    private String content;





    private publication2014c_Paragraph publication2014c_paragraph;


    public publication2014c_ReviewNote(
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

    public publication2014c_Paragraph getPublication2014c_paragraph() {
        return publication2014c_paragraph;
    }

    public void setPublication2014c_paragraph(publication2014c_Paragraph publication2014c_paragraph) {
        this.publication2014c_paragraph = publication2014c_paragraph;
    }

}