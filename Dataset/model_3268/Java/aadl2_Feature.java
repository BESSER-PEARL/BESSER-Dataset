





import java.util.List;
import java.util.ArrayList;

public class aadl2_Feature extends StructuralFeature, ArrayableElement, FeatureConnectionEnd {






    private aadl2_FlowEnd aadl2_flowend;




    private aadl2_Classifier aadl2_classifier;




    private aadl2_Feature aadl2_feature;


    public aadl2_Feature(
    ) {
        super(
        );
    }



    public aadl2_FlowEnd getAadl2_flowend() {
        return aadl2_flowend;
    }

    public void setAadl2_flowend(aadl2_FlowEnd aadl2_flowend) {
        this.aadl2_flowend = aadl2_flowend;
    }
    public aadl2_Classifier getAadl2_classifier() {
        return aadl2_classifier;
    }

    public void setAadl2_classifier(aadl2_Classifier aadl2_classifier) {
        this.aadl2_classifier = aadl2_classifier;
    }
    public aadl2_Feature getAadl2_feature() {
        return aadl2_feature;
    }

    public void setAadl2_feature(aadl2_Feature aadl2_feature) {
        this.aadl2_feature = aadl2_feature;
    }

}