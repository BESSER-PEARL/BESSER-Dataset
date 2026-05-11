





import java.util.List;
import java.util.ArrayList;

public class movies_CustomerReview extends CriticsReview {

    private String comment;



    public movies_CustomerReview(
        String comment    ) {
        super(
        );
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}