





import java.util.List;
import java.util.ArrayList;

public class researchvc_ReviewNote extends Named {

    private String content;





    private researchvc_Review researchvc_review;




    private researchvc_Paragraph researchvc_paragraph;


    public researchvc_ReviewNote(
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

    public researchvc_Review getResearchvc_review() {
        return researchvc_review;
    }

    public void setResearchvc_review(researchvc_Review researchvc_review) {
        this.researchvc_review = researchvc_review;
    }
    public researchvc_Paragraph getResearchvc_paragraph() {
        return researchvc_paragraph;
    }

    public void setResearchvc_paragraph(researchvc_Paragraph researchvc_paragraph) {
        this.researchvc_paragraph = researchvc_paragraph;
    }

}