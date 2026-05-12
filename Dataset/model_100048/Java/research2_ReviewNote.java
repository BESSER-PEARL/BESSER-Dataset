





import java.util.List;
import java.util.ArrayList;

public class research2_ReviewNote extends Named {

    private String content;





    private research2_Paragraph research2_paragraph;


    public research2_ReviewNote(
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

    public research2_Paragraph getResearch2_paragraph() {
        return research2_paragraph;
    }

    public void setResearch2_paragraph(research2_Paragraph research2_paragraph) {
        this.research2_paragraph = research2_paragraph;
    }

}