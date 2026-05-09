





import java.util.List;
import java.util.ArrayList;

public class UMLModel_SendSignalAction extends InvocationAction {

    private String signal;





    private UMLModel_InputPin umlmodel_inputpin;


    public UMLModel_SendSignalAction(
        String signal    ) {
        super(
        );
        this.signal = signal;
    }


    public String getSignal() {
        return signal;
    }

    public void setSignal(String signal) {
        this.signal = signal;
    }

    public UMLModel_InputPin getUmlmodel_inputpin() {
        return umlmodel_inputpin;
    }

    public void setUmlmodel_inputpin(UMLModel_InputPin umlmodel_inputpin) {
        this.umlmodel_inputpin = umlmodel_inputpin;
    }

}