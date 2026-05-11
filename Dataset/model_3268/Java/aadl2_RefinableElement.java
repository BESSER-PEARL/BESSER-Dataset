





import java.util.List;
import java.util.ArrayList;

public class aadl2_RefinableElement extends NamedElement {






    private aadl2_Classifier aadl2_classifier;




    private aadl2_RefinableElement aadl2_refinableelement;


    public aadl2_RefinableElement(
    ) {
        super(
        );
    }



    public aadl2_Classifier getAadl2_classifier() {
        return aadl2_classifier;
    }

    public void setAadl2_classifier(aadl2_Classifier aadl2_classifier) {
        this.aadl2_classifier = aadl2_classifier;
    }
    public aadl2_RefinableElement getAadl2_refinableelement() {
        return aadl2_refinableelement;
    }

    public void setAadl2_refinableelement(aadl2_RefinableElement aadl2_refinableelement) {
        this.aadl2_refinableelement = aadl2_refinableelement;
    }

}