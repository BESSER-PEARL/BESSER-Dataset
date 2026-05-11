





import java.util.List;
import java.util.ArrayList;

public class coCoMM_Feature  {

    private String id;
    private String name;
    private boolean abstract;
    private boolean mandatory;





    private coCoMM_FeatureModel cocomm_featuremodel;




    private coCoMM_FeatureModel cocomm_featuremodel;


    public coCoMM_Feature(
        String id,        String name,        boolean abstract,        boolean mandatory    ) {
        this.id = id;
        this.name = name;
        this.abstract = abstract;
        this.mandatory = mandatory;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
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