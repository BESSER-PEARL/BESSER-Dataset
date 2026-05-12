





import java.util.List;
import java.util.ArrayList;

public class rdal_QualityObjective extends NonFunctionalGoal {

    private String modality;
    private float bound;





    private rdal_NonFunctionalProperty rdal_nonfunctionalproperty;




    private rdal_Sensitivity rdal_sensitivity;


    public rdal_QualityObjective(
        String modality,        float bound    ) {
        super(
        );
        this.modality = modality;
        this.bound = bound;
    }


    public String getModality() {
        return modality;
    }

    public void setModality(String modality) {
        this.modality = modality;
    }
    public float getBound() {
        return bound;
    }

    public void setBound(float bound) {
        this.bound = bound;
    }

    public rdal_NonFunctionalProperty getRdal_nonfunctionalproperty() {
        return rdal_nonfunctionalproperty;
    }

    public void setRdal_nonfunctionalproperty(rdal_NonFunctionalProperty rdal_nonfunctionalproperty) {
        this.rdal_nonfunctionalproperty = rdal_nonfunctionalproperty;
    }
    public rdal_Sensitivity getRdal_sensitivity() {
        return rdal_sensitivity;
    }

    public void setRdal_sensitivity(rdal_Sensitivity rdal_sensitivity) {
        this.rdal_sensitivity = rdal_sensitivity;
    }

}