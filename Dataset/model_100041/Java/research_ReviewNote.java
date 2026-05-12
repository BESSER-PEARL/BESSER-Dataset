





import java.util.List;
import java.util.ArrayList;

public class research_ReviewNote extends Named {

    private String content;





    private research_Review research_review;


    public research_ReviewNote(
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

    public research_Review getResearch_review() {
        return research_review;
    }

    public void setResearch_review(research_Review research_review) {
        this.research_review = research_review;
    }

}