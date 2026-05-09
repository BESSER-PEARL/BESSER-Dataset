





import java.util.List;
import java.util.ArrayList;

public class reviews_Review extends Change, CommentContainer {






    private reviews_ReviewItemSet reviews_reviewitemset;




    private List<reviews_UserApprovalsMap> reviews_userapprovalsmaps;




    private List<reviews_Change> reviews_changes;




    private List<reviews_ReviewRequirementsMap> reviews_reviewrequirementsmaps;




    private List<reviews_Change> reviews_changes;




    private reviews_Comment reviews_comment;




    private List<reviews_ReviewItemSet> reviews_reviewitemsets;


    public reviews_Review(
    ) {
        super(
        );
        this.reviews_userapprovalsmaps = new ArrayList<>();
        this.reviews_changes = new ArrayList<>();
        this.reviews_reviewrequirementsmaps = new ArrayList<>();
        this.reviews_changes = new ArrayList<>();
        this.reviews_reviewitemsets = new ArrayList<>();
    }

    public reviews_Review(
        ArrayList<reviews_UserApprovalsMap> reviews_userapprovalsmaps,        ArrayList<reviews_Change> reviews_changes,        ArrayList<reviews_ReviewRequirementsMap> reviews_reviewrequirementsmaps,        ArrayList<reviews_Change> reviews_changes,        ArrayList<reviews_ReviewItemSet> reviews_reviewitemsets    ) {
        this.reviews_userapprovalsmaps = reviews_userapprovalsmaps;
        this.reviews_changes = reviews_changes;
        this.reviews_reviewrequirementsmaps = reviews_reviewrequirementsmaps;
        this.reviews_changes = reviews_changes;
        this.reviews_reviewitemsets = reviews_reviewitemsets;
    }


    public reviews_ReviewItemSet getReviews_reviewitemset() {
        return reviews_reviewitemset;
    }

    public void setReviews_reviewitemset(reviews_ReviewItemSet reviews_reviewitemset) {
        this.reviews_reviewitemset = reviews_reviewitemset;
    }
    public List<reviews_UserApprovalsMap> getReviews_userapprovalsmaps() {
        return reviews_userapprovalsmaps;
    }

    public void addReviews_userapprovalsmap(Reviews_userapprovalsmap reviews_userapprovalsmap) {
        this.reviews_userapprovalsmaps.add(reviews_userapprovalsmap);
    }
    public List<reviews_Change> getReviews_changes() {
        return reviews_changes;
    }

    public void addReviews_change(Reviews_change reviews_change) {
        this.reviews_changes.add(reviews_change);
    }
    public List<reviews_ReviewRequirementsMap> getReviews_reviewrequirementsmaps() {
        return reviews_reviewrequirementsmaps;
    }

    public void addReviews_reviewrequirementsmap(Reviews_reviewrequirementsmap reviews_reviewrequirementsmap) {
        this.reviews_reviewrequirementsmaps.add(reviews_reviewrequirementsmap);
    }
    public List<reviews_Change> getReviews_changes() {
        return reviews_changes;
    }

    public void addReviews_change(Reviews_change reviews_change) {
        this.reviews_changes.add(reviews_change);
    }
    public reviews_Comment getReviews_comment() {
        return reviews_comment;
    }

    public void setReviews_comment(reviews_Comment reviews_comment) {
        this.reviews_comment = reviews_comment;
    }
    public List<reviews_ReviewItemSet> getReviews_reviewitemsets() {
        return reviews_reviewitemsets;
    }

    public void addReviews_reviewitemset(Reviews_reviewitemset reviews_reviewitemset) {
        this.reviews_reviewitemsets.add(reviews_reviewitemset);
    }

}