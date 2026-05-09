





import java.util.List;
import java.util.ArrayList;

public class research15_ReviewNote extends Named {

    private String content;





    private research15_Review research15_review;




    private research15_Paragraph research15_paragraph;


    public research15_ReviewNote(
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

    public research15_Review getResearch15_review() {
        return research15_review;
    }

    public void setResearch15_review(research15_Review research15_review) {
        this.research15_review = research15_review;
    }
    public research15_Paragraph getResearch15_paragraph() {
        return research15_paragraph;
    }

    public void setResearch15_paragraph(research15_Paragraph research15_paragraph) {
        this.research15_paragraph = research15_paragraph;
    }

}