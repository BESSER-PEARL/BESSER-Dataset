





import java.util.List;
import java.util.ArrayList;

public class research16_ReviewNote extends Named {

    private String content;





    private research16_Review research16_review;


    public research16_ReviewNote(
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

    public research16_Review getResearch16_review() {
        return research16_review;
    }

    public void setResearch16_review(research16_Review research16_review) {
        this.research16_review = research16_review;
    }

}