





import java.util.List;
import java.util.ArrayList;

public class model_MapNameToReview  {

    private String key;





    private model_R4EReviewGroup model_r4ereviewgroup;




    private model_R4EReview model_r4ereview;


    public model_MapNameToReview(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public model_R4EReviewGroup getModel_r4ereviewgroup() {
        return model_r4ereviewgroup;
    }

    public void setModel_r4ereviewgroup(model_R4EReviewGroup model_r4ereviewgroup) {
        this.model_r4ereviewgroup = model_r4ereviewgroup;
    }
    public model_R4EReview getModel_r4ereview() {
        return model_r4ereview;
    }

    public void setModel_r4ereview(model_R4EReview model_r4ereview) {
        this.model_r4ereview = model_r4ereview;
    }

}