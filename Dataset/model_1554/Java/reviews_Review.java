





import java.util.List;
import java.util.ArrayList;

public class reviews_Review extends CommentContainer, Change {






    private List<reviews_Change> reviews_changes;




    private List<reviews_ReviewItemSet> reviews_reviewitemsets;




    private reviews_ReviewItemSet reviews_reviewitemset;




    private reviews_Comment reviews_comment;




    private List<reviews_Change> reviews_changes;


    public reviews_Review(
    ) {
        super(
        );
        this.reviews_changes = new ArrayList<>();
        this.reviews_reviewitemsets = new ArrayList<>();
        this.reviews_changes = new ArrayList<>();
    }

    public reviews_Review(
        ArrayList<reviews_Change> reviews_changes,        ArrayList<reviews_ReviewItemSet> reviews_reviewitemsets,        ArrayList<reviews_Change> reviews_changes    ) {
        this.reviews_changes = reviews_changes;
        this.reviews_reviewitemsets = reviews_reviewitemsets;
        this.reviews_changes = reviews_changes;
    }


    public List<reviews_Change> getReviews_changes() {
        return reviews_changes;
    }

    public void addReviews_change(Reviews_change reviews_change) {
        this.reviews_changes.add(reviews_change);
    }
    public List<reviews_ReviewItemSet> getReviews_reviewitemsets() {
        return reviews_reviewitemsets;
    }

    public void addReviews_reviewitemset(Reviews_reviewitemset reviews_reviewitemset) {
        this.reviews_reviewitemsets.add(reviews_reviewitemset);
    }
    public reviews_ReviewItemSet getReviews_reviewitemset() {
        return reviews_reviewitemset;
    }

    public void setReviews_reviewitemset(reviews_ReviewItemSet reviews_reviewitemset) {
        this.reviews_reviewitemset = reviews_reviewitemset;
    }
    public reviews_Comment getReviews_comment() {
        return reviews_comment;
    }

    public void setReviews_comment(reviews_Comment reviews_comment) {
        this.reviews_comment = reviews_comment;
    }
    public List<reviews_Change> getReviews_changes() {
        return reviews_changes;
    }

    public void addReviews_change(Reviews_change reviews_change) {
        this.reviews_changes.add(reviews_change);
    }

}