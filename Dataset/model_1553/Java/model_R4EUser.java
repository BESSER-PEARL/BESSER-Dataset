





import java.util.List;
import java.util.ArrayList;

public class model_R4EUser extends R4EReviewComponent, User {

    private String groupPaths;
    private int reviewCompletedCode;
    private int sequenceIDCounter;
    private boolean reviewCompleted;
    private boolean reviewCreatedByMe;





    private model_R4EReview model_r4ereview;




    private model_R4EReview model_r4ereview;




    private List<model_R4EComment> model_r4ecomments;


    public model_R4EUser(
        String groupPaths,        int reviewCompletedCode,        int sequenceIDCounter,        boolean reviewCompleted,        boolean reviewCreatedByMe    ) {
        super(
        );
        this.groupPaths = groupPaths;
        this.reviewCompletedCode = reviewCompletedCode;
        this.sequenceIDCounter = sequenceIDCounter;
        this.reviewCompleted = reviewCompleted;
        this.reviewCreatedByMe = reviewCreatedByMe;
        this.model_r4ecomments = new ArrayList<>();
    }

    public model_R4EUser(
        String groupPaths,        int reviewCompletedCode,        int sequenceIDCounter,        boolean reviewCompleted,        boolean reviewCreatedByMe        ArrayList<model_R4EComment> model_r4ecomments    ) {
        this.groupPaths = groupPaths;
        this.reviewCompletedCode = reviewCompletedCode;
        this.sequenceIDCounter = sequenceIDCounter;
        this.reviewCompleted = reviewCompleted;
        this.reviewCreatedByMe = reviewCreatedByMe;
        this.model_r4ecomments = model_r4ecomments;
    }

    public String getGrouppaths() {
        return groupPaths;
    }

    public void setGrouppaths(String groupPaths) {
        this.groupPaths = groupPaths;
    }
    public int getReviewcompletedcode() {
        return reviewCompletedCode;
    }

    public void setReviewcompletedcode(int reviewCompletedCode) {
        this.reviewCompletedCode = reviewCompletedCode;
    }
    public int getSequenceidcounter() {
        return sequenceIDCounter;
    }

    public void setSequenceidcounter(int sequenceIDCounter) {
        this.sequenceIDCounter = sequenceIDCounter;
    }
    public boolean getReviewcompleted() {
        return reviewCompleted;
    }

    public void setReviewcompleted(boolean reviewCompleted) {
        this.reviewCompleted = reviewCompleted;
    }
    public boolean getReviewcreatedbyme() {
        return reviewCreatedByMe;
    }

    public void setReviewcreatedbyme(boolean reviewCreatedByMe) {
        this.reviewCreatedByMe = reviewCreatedByMe;
    }

    public model_R4EReview getModel_r4ereview() {
        return model_r4ereview;
    }

    public void setModel_r4ereview(model_R4EReview model_r4ereview) {
        this.model_r4ereview = model_r4ereview;
    }
    public model_R4EReview getModel_r4ereview() {
        return model_r4ereview;
    }

    public void setModel_r4ereview(model_R4EReview model_r4ereview) {
        this.model_r4ereview = model_r4ereview;
    }
    public List<model_R4EComment> getModel_r4ecomments() {
        return model_r4ecomments;
    }

    public void addModel_r4ecomment(Model_r4ecomment model_r4ecomment) {
        this.model_r4ecomments.add(model_r4ecomment);
    }

}