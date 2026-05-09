





import java.util.List;
import java.util.ArrayList;

public class model_R4EAnomalyType extends CommentType {

    private String type;





    private model_R4EReviewGroup model_r4ereviewgroup;


    public model_R4EAnomalyType(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public model_R4EReviewGroup getModel_r4ereviewgroup() {
        return model_r4ereviewgroup;
    }

    public void setModel_r4ereviewgroup(model_R4EReviewGroup model_r4ereviewgroup) {
        this.model_r4ereviewgroup = model_r4ereviewgroup;
    }

}