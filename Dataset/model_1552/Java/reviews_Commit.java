





import java.util.List;
import java.util.ArrayList;

public class reviews_Commit  {

    private String id;
    private String subject;





    private reviews_ReviewItemSet reviews_reviewitemset;


    public reviews_Commit(
        String id,        String subject    ) {
        this.id = id;
        this.subject = subject;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public reviews_ReviewItemSet getReviews_reviewitemset() {
        return reviews_reviewitemset;
    }

    public void setReviews_reviewitemset(reviews_ReviewItemSet reviews_reviewitemset) {
        this.reviews_reviewitemset = reviews_reviewitemset;
    }

}