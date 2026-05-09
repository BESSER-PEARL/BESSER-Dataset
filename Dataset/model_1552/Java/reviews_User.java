





import java.util.List;
import java.util.ArrayList;

public class reviews_User  {

    private String displayName;
    private String email;
    private String id;





    private reviews_UserApprovalsMap reviews_userapprovalsmap;




    private reviews_Change reviews_change;




    private reviews_Comment reviews_comment;


    public reviews_User(
        String displayName,        String email,        String id    ) {
        this.displayName = displayName;
        this.email = email;
        this.id = id;
    }


    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
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

    public reviews_UserApprovalsMap getReviews_userapprovalsmap() {
        return reviews_userapprovalsmap;
    }

    public void setReviews_userapprovalsmap(reviews_UserApprovalsMap reviews_userapprovalsmap) {
        this.reviews_userapprovalsmap = reviews_userapprovalsmap;
    }
    public reviews_Change getReviews_change() {
        return reviews_change;
    }

    public void setReviews_change(reviews_Change reviews_change) {
        this.reviews_change = reviews_change;
    }
    public reviews_Comment getReviews_comment() {
        return reviews_comment;
    }

    public void setReviews_comment(reviews_Comment reviews_comment) {
        this.reviews_comment = reviews_comment;
    }

}