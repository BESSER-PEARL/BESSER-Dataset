





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentPrototype extends FeatureClassifier, SubcomponentType, Prototype {

    private String array;





    private aadl2_Feature aadl2_feature;




    private aadl2_Subcomponent aadl2_subcomponent;




    private aadl2_ComponentClassifier aadl2_componentclassifier;


    public aadl2_ComponentPrototype(
        String array    ) {
        super(
        );
        this.array = array;
    }


    public String getArray() {
        return array;
    }

    public void setArray(String array) {
        this.array = array;
    }

    public aadl2_Feature getAadl2_feature() {
        return aadl2_feature;
    }

    public void setAadl2_feature(aadl2_Feature aadl2_feature) {
        this.aadl2_feature = aadl2_feature;
    }
    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }
    public aadl2_ComponentClassifier getAadl2_componentclassifier() {
        return aadl2_componentclassifier;
    }

    public void setAadl2_componentclassifier(aadl2_ComponentClassifier aadl2_componentclassifier) {
        this.aadl2_componentclassifier = aadl2_componentclassifier;
    }

}