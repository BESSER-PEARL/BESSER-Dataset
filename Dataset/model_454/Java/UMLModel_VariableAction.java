





import java.util.List;
import java.util.ArrayList;

public class UMLModel_VariableAction extends Action {

    private String variable;



    public UMLModel_VariableAction(
        String variable    ) {
        super(
        );
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }


}