




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_R4EComment extends R4EIDComponent, R4EReviewComponent, Comment {

    private LocalDate createdOn;





    private model_R4EAnomaly model_r4eanomaly;


    public model_R4EComment(
        LocalDate createdOn    ) {
        super(
        );
        this.createdOn = createdOn;
    }


    public LocalDate getCreatedon() {
        return createdOn;
    }

    public void setCreatedon(LocalDate createdOn) {
        this.createdOn = createdOn;
    }

    public model_R4EAnomaly getModel_r4eanomaly() {
        return model_r4eanomaly;
    }

    public void setModel_r4eanomaly(model_R4EAnomaly model_r4eanomaly) {
        this.model_r4eanomaly = model_r4eanomaly;
    }

}