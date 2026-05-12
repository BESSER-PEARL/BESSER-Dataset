





import java.util.List;
import java.util.ArrayList;

public class Review  {

    private String comments;
    private int rating;
    private int reviewId;



    public Review(
        String comments,        int rating,        int reviewId    ) {
        this.comments = comments;
        this.rating = rating;
        this.reviewId = reviewId;
    }


    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }
    public int getReviewid() {
        return reviewId;
    }

    public void setReviewid(int reviewId) {
        this.reviewId = reviewId;
    }


}