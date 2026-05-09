





import java.util.List;
import java.util.ArrayList;

public class research19_ReviewNote extends Named {

    private String content;





    private research19_Review research19_review;




    private research19_Paragraph research19_paragraph;


    public research19_ReviewNote(
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

    public research19_Review getResearch19_review() {
        return research19_review;
    }

    public void setResearch19_review(research19_Review research19_review) {
        this.research19_review = research19_review;
    }
    public research19_Paragraph getResearch19_paragraph() {
        return research19_paragraph;
    }

    public void setResearch19_paragraph(research19_Paragraph research19_paragraph) {
        this.research19_paragraph = research19_paragraph;
    }

}