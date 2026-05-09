





import java.util.List;
import java.util.ArrayList;

public class research101_ReviewNote extends Named {

    private String content;





    private research101_Review research101_review;


    public research101_ReviewNote(
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

    public research101_Review getResearch101_review() {
        return research101_review;
    }

    public void setResearch101_review(research101_Review research101_review) {
        this.research101_review = research101_review;
    }

}