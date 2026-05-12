





import java.util.List;
import java.util.ArrayList;

public class UML2_ReadIsClassifiedObjectAction extends Action {

    private boolean isDirect;





    private UML2_OutputPin uml2_outputpin;




    private UML2_Classifier uml2_classifier;




    private UML2_InputPin uml2_inputpin;


    public UML2_ReadIsClassifiedObjectAction(
        boolean isDirect    ) {
        super(
        );
        this.isDirect = isDirect;
    }


    public boolean getIsdirect() {
        return isDirect;
    }

    public void setIsdirect(boolean isDirect) {
        this.isDirect = isDirect;
    }

    public UML2_OutputPin getUml2_outputpin() {
        return uml2_outputpin;
    }

    public void setUml2_outputpin(UML2_OutputPin uml2_outputpin) {
        this.uml2_outputpin = uml2_outputpin;
    }
    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public UML2_InputPin getUml2_inputpin() {
        return uml2_inputpin;
    }

    public void setUml2_inputpin(UML2_InputPin uml2_inputpin) {
        this.uml2_inputpin = uml2_inputpin;
    }

}