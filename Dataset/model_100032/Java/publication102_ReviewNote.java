





import java.util.List;
import java.util.ArrayList;

public class publication102_ReviewNote extends Named {

    private String content;





    private publication102_Review publication102_review;


    public publication102_ReviewNote(
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

    public publication102_Review getPublication102_review() {
        return publication102_review;
    }

    public void setPublication102_review(publication102_Review publication102_review) {
        this.publication102_review = publication102_review;
    }

}