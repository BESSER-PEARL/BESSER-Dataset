





import java.util.List;
import java.util.ArrayList;

public class db_CriticsReviewType  {

    private String rating;
    private String reviewedBy;





    private db_DocumentRoot db_documentroot;


    public db_CriticsReviewType(
        String rating,        String reviewedBy    ) {
        this.rating = rating;
        this.reviewedBy = reviewedBy;
    }


    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }
    public String getReviewedby() {
        return reviewedBy;
    }

    public void setReviewedby(String reviewedBy) {
        this.reviewedBy = reviewedBy;
    }

    public db_DocumentRoot getDb_documentroot() {
        return db_documentroot;
    }

    public void setDb_documentroot(db_DocumentRoot db_documentroot) {
        this.db_documentroot = db_documentroot;
    }

}