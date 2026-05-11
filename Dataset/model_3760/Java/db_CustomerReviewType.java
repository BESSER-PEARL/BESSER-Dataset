





import java.util.List;
import java.util.ArrayList;

public class db_CustomerReviewType extends CriticsReviewType {

    private String comment;



    public db_CustomerReviewType(
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