





import java.util.List;
import java.util.ArrayList;

public class reviews_ApprovalType  {

    private String key;
    private String name;





    private reviews_Repository reviews_repository;




    private reviews_ReviewRequirementsMap reviews_reviewrequirementsmap;


    public reviews_ApprovalType(
        String key,        String name    ) {
        this.key = key;
        this.name = name;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public reviews_Repository getReviews_repository() {
        return reviews_repository;
    }

    public void setReviews_repository(reviews_Repository reviews_repository) {
        this.reviews_repository = reviews_repository;
    }
    public reviews_ReviewRequirementsMap getReviews_reviewrequirementsmap() {
        return reviews_reviewrequirementsmap;
    }

    public void setReviews_reviewrequirementsmap(reviews_ReviewRequirementsMap reviews_reviewrequirementsmap) {
        this.reviews_reviewrequirementsmap = reviews_reviewrequirementsmap;
    }

}