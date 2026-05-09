





import java.util.List;
import java.util.ArrayList;

public class UMLModel_AddVariableValueAction extends WriteVariableAction {

    private String isReplaceAll;





    private UMLModel_InputPin umlmodel_inputpin;


    public UMLModel_AddVariableValueAction(
        String isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
    }


    public String getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(String isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public UMLModel_InputPin getUmlmodel_inputpin() {
        return umlmodel_inputpin;
    }

    public void setUmlmodel_inputpin(UMLModel_InputPin umlmodel_inputpin) {
        this.umlmodel_inputpin = umlmodel_inputpin;
    }

}