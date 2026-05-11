





import java.util.List;
import java.util.ArrayList;

public class robochart_LambdaExp extends Expression {






    private robochart_Expression robochart_expression;




    private List<robochart_Variable> robochart_variables;




    private robochart_Expression robochart_expression;


    public robochart_LambdaExp(
    ) {
        super(
        );
        this.robochart_variables = new ArrayList<>();
    }

    public robochart_LambdaExp(
        ArrayList<robochart_Variable> robochart_variables    ) {
        this.robochart_variables = robochart_variables;
    }


    public robochart_Expression getRobochart_expression() {
        return robochart_expression;
    }

    public void setRobochart_expression(robochart_Expression robochart_expression) {
        this.robochart_expression = robochart_expression;
    }
    public List<robochart_Variable> getRobochart_variables() {
        return robochart_variables;
    }

    public void addRobochart_variable(Robochart_variable robochart_variable) {
        this.robochart_variables.add(robochart_variable);
    }
    public robochart_Expression getRobochart_expression() {
        return robochart_expression;
    }

    public void setRobochart_expression(robochart_Expression robochart_expression) {
        this.robochart_expression = robochart_expression;
    }

}