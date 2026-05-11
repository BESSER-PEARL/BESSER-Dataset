





import java.util.List;
import java.util.ArrayList;

public class klangexpr_VariableAssignment extends Statement {

    private String variableName;



    public klangexpr_VariableAssignment(
        String variableName    ) {
        super(
        );
        this.variableName = variableName;
    }


    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }


}