





import java.util.List;
import java.util.ArrayList;

public class Cocus_Reviewer extends ConferenceMember, User {






    private ExternalReviewer externalreviewer;




    private Paper paper;




    private Paper paper;




    private Review review;




    private Bid bid;


    public Cocus_Reviewer(
    ) {
        super(
        );
    }



    public ExternalReviewer getExternalreviewer() {
        return externalreviewer;
    }

    public void setExternalreviewer(ExternalReviewer externalreviewer) {
        this.externalreviewer = externalreviewer;
    }
    public Paper getPaper() {
        return paper;
    }

    public void setPaper(Paper paper) {
        this.paper = paper;
    }
    public Paper getPaper() {
        return paper;
    }

    public void setPaper(Paper paper) {
        this.paper = paper;
    }
    public Review getReview() {
        return review;
    }

    public void setReview(Review review) {
        this.review = review;
    }
    public Bid getBid() {
        return bid;
    }

    public void setBid(Bid bid) {
        this.bid = bid;
    }

}