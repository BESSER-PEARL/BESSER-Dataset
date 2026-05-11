





import java.util.List;
import java.util.ArrayList;

public class klangexpr_VariableReference extends Expression {

    private String variableName;



    public klangexpr_VariableReference(
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