





import java.util.List;
import java.util.ArrayList;

public class researchva_ReviewNote extends Named {

    private String content;





    private researchva_Review researchva_review;


    public researchva_ReviewNote(
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

    public researchva_Review getResearchva_review() {
        return researchva_review;
    }

    public void setResearchva_review(researchva_Review researchva_review) {
        this.researchva_review = researchva_review;
    }

}