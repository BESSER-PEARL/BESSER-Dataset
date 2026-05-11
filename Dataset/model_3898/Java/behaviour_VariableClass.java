





import java.util.List;
import java.util.ArrayList;

public class behaviour_VariableClass extends Expression {

    private String variableName;



    public behaviour_VariableClass(
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