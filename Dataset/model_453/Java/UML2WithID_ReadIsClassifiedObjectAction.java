





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ReadIsClassifiedObjectAction extends Action {

    private boolean isDirect;





    private UML2WithID_OutputPin uml2withid_outputpin;




    private UML2WithID_InputPin uml2withid_inputpin;




    private UML2WithID_Classifier uml2withid_classifier;


    public UML2WithID_ReadIsClassifiedObjectAction(
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

    public UML2WithID_OutputPin getUml2withid_outputpin() {
        return uml2withid_outputpin;
    }

    public void setUml2withid_outputpin(UML2WithID_OutputPin uml2withid_outputpin) {
        this.uml2withid_outputpin = uml2withid_outputpin;
    }
    public UML2WithID_InputPin getUml2withid_inputpin() {
        return uml2withid_inputpin;
    }

    public void setUml2withid_inputpin(UML2WithID_InputPin uml2withid_inputpin) {
        this.uml2withid_inputpin = uml2withid_inputpin;
    }
    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }

}