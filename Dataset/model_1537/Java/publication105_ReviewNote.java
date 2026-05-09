





import java.util.List;
import java.util.ArrayList;

public class publication105_ReviewNote extends Named {

    private String content;





    private publication105_Review publication105_review;


    public publication105_ReviewNote(
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

    public publication105_Review getPublication105_review() {
        return publication105_review;
    }

    public void setPublication105_review(publication105_Review publication105_review) {
        this.publication105_review = publication105_review;
    }

}