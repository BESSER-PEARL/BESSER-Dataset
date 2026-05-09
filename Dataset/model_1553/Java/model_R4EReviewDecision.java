





import java.util.List;
import java.util.ArrayList;

public class model_R4EReviewDecision  {

    private int spentTime;
    private String value;





    private model_R4EReview model_r4ereview;


    public model_R4EReviewDecision(
        int spentTime,        String value    ) {
        this.spentTime = spentTime;
        this.value = value;
    }


    public int getSpenttime() {
        return spentTime;
    }

    public void setSpenttime(int spentTime) {
        this.spentTime = spentTime;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public model_R4EReview getModel_r4ereview() {
        return model_r4ereview;
    }

    public void setModel_r4ereview(model_R4EReview model_r4ereview) {
        this.model_r4ereview = model_r4ereview;
    }

}