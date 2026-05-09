





import java.util.List;
import java.util.ArrayList;

public class model_MapToUsers  {

    private String key;





    private model_R4EUser model_r4euser;




    private model_R4EReview model_r4ereview;


    public model_MapToUsers(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public model_R4EUser getModel_r4euser() {
        return model_r4euser;
    }

    public void setModel_r4euser(model_R4EUser model_r4euser) {
        this.model_r4euser = model_r4euser;
    }
    public model_R4EReview getModel_r4ereview() {
        return model_r4ereview;
    }

    public void setModel_r4ereview(model_R4EReview model_r4ereview) {
        this.model_r4ereview = model_r4ereview;
    }

}