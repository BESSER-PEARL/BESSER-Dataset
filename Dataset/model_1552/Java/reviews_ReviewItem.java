





import java.util.List;
import java.util.ArrayList;

public class reviews_ReviewItem extends CommentContainer {

    private String name;
    private String reference;
    private String id;





    private reviews_Review reviews_review;




    private reviews_User reviews_user;




    private reviews_User reviews_user;


    public reviews_ReviewItem(
        String name,        String reference,        String id    ) {
        super(
        );
        this.name = name;
        this.reference = reference;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public reviews_Review getReviews_review() {
        return reviews_review;
    }

    public void setReviews_review(reviews_Review reviews_review) {
        this.reviews_review = reviews_review;
    }
    public reviews_User getReviews_user() {
        return reviews_user;
    }

    public void setReviews_user(reviews_User reviews_user) {
        this.reviews_user = reviews_user;
    }
    public reviews_User getReviews_user() {
        return reviews_user;
    }

    public void setReviews_user(reviews_User reviews_user) {
        this.reviews_user = reviews_user;
    }

}