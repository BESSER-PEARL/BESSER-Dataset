





import java.util.List;
import java.util.ArrayList;

public class iot2_Expression_VariableName extends Expression {

    private boolean variable;



    public iot2_Expression_VariableName(
        boolean variable    ) {
        super(
        );
        this.variable = variable;
    }


    public boolean getVariable() {
        return variable;
    }

    public void setVariable(boolean variable) {
        this.variable = variable;
    }


}