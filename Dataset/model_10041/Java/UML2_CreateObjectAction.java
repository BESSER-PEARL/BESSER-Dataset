





import java.util.List;
import java.util.ArrayList;

public class UML2_CreateObjectAction extends Action {






    private UML2_Classifier uml2_classifier;




    private UML2_OutputPin uml2_outputpin;


    public UML2_CreateObjectAction(
    ) {
        super(
        );
    }



    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public UML2_OutputPin getUml2_outputpin() {
        return uml2_outputpin;
    }

    public void setUml2_outputpin(UML2_OutputPin uml2_outputpin) {
        this.uml2_outputpin = uml2_outputpin;
    }

}