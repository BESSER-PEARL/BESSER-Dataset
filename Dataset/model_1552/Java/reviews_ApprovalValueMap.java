





import java.util.List;
import java.util.ArrayList;

public class reviews_ApprovalValueMap  {

    private String value;





    private reviews_ApprovalType reviews_approvaltype;




    private reviews_ReviewerEntry reviews_reviewerentry;


    public reviews_ApprovalValueMap(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public reviews_ApprovalType getReviews_approvaltype() {
        return reviews_approvaltype;
    }

    public void setReviews_approvaltype(reviews_ApprovalType reviews_approvaltype) {
        this.reviews_approvaltype = reviews_approvaltype;
    }
    public reviews_ReviewerEntry getReviews_reviewerentry() {
        return reviews_reviewerentry;
    }

    public void setReviews_reviewerentry(reviews_ReviewerEntry reviews_reviewerentry) {
        this.reviews_reviewerentry = reviews_reviewerentry;
    }

}