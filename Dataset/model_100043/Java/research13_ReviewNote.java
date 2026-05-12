





import java.util.List;
import java.util.ArrayList;

public class research13_ReviewNote extends Named {

    private String content;





    private research13_Review research13_review;


    public research13_ReviewNote(
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

    public research13_Review getResearch13_review() {
        return research13_review;
    }

    public void setResearch13_review(research13_Review research13_review) {
        this.research13_review = research13_review;
    }

}