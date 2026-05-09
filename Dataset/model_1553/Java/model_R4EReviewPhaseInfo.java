




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_R4EReviewPhaseInfo  {

    private LocalDate endDate;
    private String phaseOwnerID;
    private LocalDate startDate;
    private String type;





    private model_R4EFormalReview model_r4eformalreview;




    private model_R4EFormalReview model_r4eformalreview;


    public model_R4EReviewPhaseInfo(
        LocalDate endDate,        String phaseOwnerID,        LocalDate startDate,        String type    ) {
        this.endDate = endDate;
        this.phaseOwnerID = phaseOwnerID;
        this.startDate = startDate;
        this.type = type;
    }


    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public String getPhaseownerid() {
        return phaseOwnerID;
    }

    public void setPhaseownerid(String phaseOwnerID) {
        this.phaseOwnerID = phaseOwnerID;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public model_R4EFormalReview getModel_r4eformalreview() {
        return model_r4eformalreview;
    }

    public void setModel_r4eformalreview(model_R4EFormalReview model_r4eformalreview) {
        this.model_r4eformalreview = model_r4eformalreview;
    }
    public model_R4EFormalReview getModel_r4eformalreview() {
        return model_r4eformalreview;
    }

    public void setModel_r4eformalreview(model_R4EFormalReview model_r4eformalreview) {
        this.model_r4eformalreview = model_r4eformalreview;
    }

}