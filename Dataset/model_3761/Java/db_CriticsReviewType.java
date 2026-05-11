





import java.util.List;
import java.util.ArrayList;

public class db_CriticsReviewType  {

    private String rating;
    private String reviewedBy;



    public db_CriticsReviewType(
        String rating,        String reviewedBy    ) {
        this.rating = rating;
        this.reviewedBy = reviewedBy;
    }


    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }
    public String getReviewedby() {
        return reviewedBy;
    }

    public void setReviewedby(String reviewedBy) {
        this.reviewedBy = reviewedBy;
    }


}