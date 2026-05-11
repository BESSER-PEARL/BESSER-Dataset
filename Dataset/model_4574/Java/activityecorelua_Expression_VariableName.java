





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Expression_VariableName extends Expression {

    private String variable;



    public activityecorelua_Expression_VariableName(
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