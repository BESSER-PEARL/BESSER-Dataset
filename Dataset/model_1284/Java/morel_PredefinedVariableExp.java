





import java.util.List;
import java.util.ArrayList;

public class morel_PredefinedVariableExp extends AtomicExp {

    private String variable;



    public morel_PredefinedVariableExp(
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