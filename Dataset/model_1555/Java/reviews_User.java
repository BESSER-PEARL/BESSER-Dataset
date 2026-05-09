





import java.util.List;
import java.util.ArrayList;

public class reviews_User  {

    private String email;
    private String id;
    private String displayName;





    private reviews_Comment reviews_comment;




    private reviews_ReviewItem reviews_reviewitem;




    private reviews_Change reviews_change;




    private reviews_ReviewItem reviews_reviewitem;


    public reviews_User(
        String email,        String id,        String displayName    ) {
        this.email = email;
        this.id = id;
        this.displayName = displayName;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }

    public reviews_Comment getReviews_comment() {
        return reviews_comment;
    }

    public void setReviews_comment(reviews_Comment reviews_comment) {
        this.reviews_comment = reviews_comment;
    }
    public reviews_ReviewItem getReviews_reviewitem() {
        return reviews_reviewitem;
    }

    public void setReviews_reviewitem(reviews_ReviewItem reviews_reviewitem) {
        this.reviews_reviewitem = reviews_reviewitem;
    }
    public reviews_Change getReviews_change() {
        return reviews_change;
    }

    public void setReviews_change(reviews_Change reviews_change) {
        this.reviews_change = reviews_change;
    }
    public reviews_ReviewItem getReviews_reviewitem() {
        return reviews_reviewitem;
    }

    public void setReviews_reviewitem(reviews_ReviewItem reviews_reviewitem) {
        this.reviews_reviewitem = reviews_reviewitem;
    }

}