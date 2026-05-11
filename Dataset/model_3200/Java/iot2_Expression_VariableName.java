





import java.util.List;
import java.util.ArrayList;

public class iot2_Expression_VariableName extends Expression {

    private String variable;



    public iot2_Expression_VariableName(
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