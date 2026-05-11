





import java.util.List;
import java.util.ArrayList;

public class movies_CriticsReview  {

    private String reviewedBy;
    private String rating;



    public movies_CriticsReview(
        String reviewedBy,        String rating    ) {
        this.reviewedBy = reviewedBy;
        this.rating = rating;
    }


    public String getReviewedby() {
        return reviewedBy;
    }

    public void setReviewedby(String reviewedBy) {
        this.reviewedBy = reviewedBy;
    }
    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }


}