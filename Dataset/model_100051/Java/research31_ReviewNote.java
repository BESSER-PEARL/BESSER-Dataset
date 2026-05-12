





import java.util.List;
import java.util.ArrayList;

public class research31_ReviewNote extends Named {

    private String content;





    private research31_Paragraph research31_paragraph;




    private research31_Review research31_review;


    public research31_ReviewNote(
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

    public research31_Paragraph getResearch31_paragraph() {
        return research31_paragraph;
    }

    public void setResearch31_paragraph(research31_Paragraph research31_paragraph) {
        this.research31_paragraph = research31_paragraph;
    }
    public research31_Review getResearch31_review() {
        return research31_review;
    }

    public void setResearch31_review(research31_Review research31_review) {
        this.research31_review = research31_review;
    }

}