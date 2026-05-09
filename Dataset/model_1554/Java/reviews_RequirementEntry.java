





import java.util.List;
import java.util.ArrayList;

public class reviews_RequirementEntry  {

    private String status;





    private reviews_ReviewRequirementsMap reviews_reviewrequirementsmap;




    private reviews_User reviews_user;


    public reviews_RequirementEntry(
        String status    ) {
        this.status = status;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public reviews_ReviewRequirementsMap getReviews_reviewrequirementsmap() {
        return reviews_reviewrequirementsmap;
    }

    public void setReviews_reviewrequirementsmap(reviews_ReviewRequirementsMap reviews_reviewrequirementsmap) {
        this.reviews_reviewrequirementsmap = reviews_reviewrequirementsmap;
    }
    public reviews_User getReviews_user() {
        return reviews_user;
    }

    public void setReviews_user(reviews_User reviews_user) {
        this.reviews_user = reviews_user;
    }

}