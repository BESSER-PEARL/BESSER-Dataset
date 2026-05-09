





import java.util.List;
import java.util.ArrayList;

public class reviews_ReviewItem extends CommentContainer {

    private String reference;
    private String name;
    private String id;





    private reviews_Review reviews_review;


    public reviews_ReviewItem(
        String reference,        String name,        String id    ) {
        super(
        );
        this.reference = reference;
        this.name = name;
        this.id = id;
    }


    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

}