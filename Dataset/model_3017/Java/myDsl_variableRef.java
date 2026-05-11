





import java.util.List;
import java.util.ArrayList;

public class myDsl_variableRef extends simple_expression {

    private String variable;



    public myDsl_variableRef(
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