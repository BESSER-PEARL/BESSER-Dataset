





import java.util.List;
import java.util.ArrayList;

public class gastm_FunctionCallExpression extends Expression {






    private gastm_Expression gastm_expression;




    private List<gastm_ActualParameter> gastm_actualparameters;


    public gastm_FunctionCallExpression(
    ) {
        super(
        );
        this.gastm_actualparameters = new ArrayList<>();
    }

    public gastm_FunctionCallExpression(
        ArrayList<gastm_ActualParameter> gastm_actualparameters    ) {
        this.gastm_actualparameters = gastm_actualparameters;
    }


    public gastm_Expression getGastm_expression() {
        return gastm_expression;
    }

    public void setGastm_expression(gastm_Expression gastm_expression) {
        this.gastm_expression = gastm_expression;
    }
    public List<gastm_ActualParameter> getGastm_actualparameters() {
        return gastm_actualparameters;
    }

    public void addGastm_actualparameter(Gastm_actualparameter gastm_actualparameter) {
        this.gastm_actualparameters.add(gastm_actualparameter);
    }

}