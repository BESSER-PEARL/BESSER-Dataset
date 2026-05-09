





import java.util.List;
import java.util.ArrayList;

public class UMLModel_CallOperationAction extends CallAction {

    private String operation;





    private UMLModel_InputPin umlmodel_inputpin;


    public UMLModel_CallOperationAction(
        String operation    ) {
        super(
        );
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public UMLModel_InputPin getUmlmodel_inputpin() {
        return umlmodel_inputpin;
    }

    public void setUmlmodel_inputpin(UMLModel_InputPin umlmodel_inputpin) {
        this.umlmodel_inputpin = umlmodel_inputpin;
    }

}