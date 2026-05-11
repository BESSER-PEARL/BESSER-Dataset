





import java.util.List;
import java.util.ArrayList;

public class coCoMM_Feature  {

    private String name;
    private String id;
    private boolean mandatory;
    private boolean abstract;





    private coCoMM_FeatureModel cocomm_featuremodel;




    private coCoMM_FeatureModel cocomm_featuremodel;


    public coCoMM_Feature(
        String name,        String id,        boolean mandatory,        boolean abstract    ) {
        this.name = name;
        this.id = id;
        this.mandatory = mandatory;
        this.abstract = abstract;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public coCoMM_FeatureModel getCocomm_featuremodel() {
        return cocomm_featuremodel;
    }

    public void setCocomm_featuremodel(coCoMM_FeatureModel cocomm_featuremodel) {
        this.cocomm_featuremodel = cocomm_featuremodel;
    }
    public coCoMM_FeatureModel getCocomm_featuremodel() {
        return cocomm_featuremodel;
    }

    public void setCocomm_featuremodel(coCoMM_FeatureModel cocomm_featuremodel) {
        this.cocomm_featuremodel = cocomm_featuremodel;
    }

}