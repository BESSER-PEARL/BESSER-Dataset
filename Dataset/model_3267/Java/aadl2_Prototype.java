





import java.util.List;
import java.util.ArrayList;

public class aadl2_Prototype extends StructuralFeature, CalledSubprogram {






    private aadl2_Prototype aadl2_prototype;




    private aadl2_Classifier aadl2_classifier;




    private aadl2_PrototypeBinding aadl2_prototypebinding;


    public aadl2_Prototype(
    ) {
        super(
        );
    }



    public aadl2_Prototype getAadl2_prototype() {
        return aadl2_prototype;
    }

    public void setAadl2_prototype(aadl2_Prototype aadl2_prototype) {
        this.aadl2_prototype = aadl2_prototype;
    }
    public aadl2_Classifier getAadl2_classifier() {
        return aadl2_classifier;
    }

    public void setAadl2_classifier(aadl2_Classifier aadl2_classifier) {
        this.aadl2_classifier = aadl2_classifier;
    }
    public aadl2_PrototypeBinding getAadl2_prototypebinding() {
        return aadl2_prototypebinding;
    }

    public void setAadl2_prototypebinding(aadl2_PrototypeBinding aadl2_prototypebinding) {
        this.aadl2_prototypebinding = aadl2_prototypebinding;
    }

}