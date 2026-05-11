





import java.util.List;
import java.util.ArrayList;

public class aadl2_FeaturePrototype extends Prototype {

    private String direction;





    private aadl2_FeaturePrototypeReference aadl2_featureprototypereference;




    private aadl2_AbstractFeature aadl2_abstractfeature;




    private aadl2_ComponentClassifier aadl2_componentclassifier;


    public aadl2_FeaturePrototype(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public aadl2_FeaturePrototypeReference getAadl2_featureprototypereference() {
        return aadl2_featureprototypereference;
    }

    public void setAadl2_featureprototypereference(aadl2_FeaturePrototypeReference aadl2_featureprototypereference) {
        this.aadl2_featureprototypereference = aadl2_featureprototypereference;
    }
    public aadl2_AbstractFeature getAadl2_abstractfeature() {
        return aadl2_abstractfeature;
    }

    public void setAadl2_abstractfeature(aadl2_AbstractFeature aadl2_abstractfeature) {
        this.aadl2_abstractfeature = aadl2_abstractfeature;
    }
    public aadl2_ComponentClassifier getAadl2_componentclassifier() {
        return aadl2_componentclassifier;
    }

    public void setAadl2_componentclassifier(aadl2_ComponentClassifier aadl2_componentclassifier) {
        this.aadl2_componentclassifier = aadl2_componentclassifier;
    }

}