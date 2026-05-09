





import java.util.List;
import java.util.ArrayList;

public class UMLModel_RemoveVariableValueAction extends WriteVariableAction {

    private String isRemoveDuplicates;





    private UMLModel_InputPin umlmodel_inputpin;


    public UMLModel_RemoveVariableValueAction(
        String isRemoveDuplicates    ) {
        super(
        );
        this.isRemoveDuplicates = isRemoveDuplicates;
    }


    public String getIsremoveduplicates() {
        return isRemoveDuplicates;
    }

    public void setIsremoveduplicates(String isRemoveDuplicates) {
        this.isRemoveDuplicates = isRemoveDuplicates;
    }

    public UMLModel_InputPin getUmlmodel_inputpin() {
        return umlmodel_inputpin;
    }

    public void setUmlmodel_inputpin(UMLModel_InputPin umlmodel_inputpin) {
        this.umlmodel_inputpin = umlmodel_inputpin;
    }

}