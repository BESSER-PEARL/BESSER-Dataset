





import java.util.List;
import java.util.ArrayList;

public class robochart_QuantifierExpression extends Expression {






    private List<robochart_Variable> robochart_variables;


    public robochart_QuantifierExpression(
    ) {
        super(
        );
        this.robochart_variables = new ArrayList<>();
    }

    public robochart_QuantifierExpression(
        ArrayList<robochart_Variable> robochart_variables    ) {
        this.robochart_variables = robochart_variables;
    }


    public List<robochart_Variable> getRobochart_variables() {
        return robochart_variables;
    }

    public void addRobochart_variable(Robochart_variable robochart_variable) {
        this.robochart_variables.add(robochart_variable);
    }

}