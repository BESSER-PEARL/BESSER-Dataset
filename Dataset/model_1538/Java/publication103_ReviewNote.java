





import java.util.List;
import java.util.ArrayList;

public class publication103_ReviewNote extends Named {

    private String content;





    private publication103_Review publication103_review;


    public publication103_ReviewNote(
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

    public publication103_Review getPublication103_review() {
        return publication103_review;
    }

    public void setPublication103_review(publication103_Review publication103_review) {
        this.publication103_review = publication103_review;
    }

}