





import java.util.List;
import java.util.ArrayList;

public class astm_FunctionCallExpression extends Expression {






    private astm_Expression astm_expression;




    private List<astm_ActualParameter> astm_actualparameters;


    public astm_FunctionCallExpression(
    ) {
        super(
        );
        this.astm_actualparameters = new ArrayList<>();
    }

    public astm_FunctionCallExpression(
        ArrayList<astm_ActualParameter> astm_actualparameters    ) {
        this.astm_actualparameters = astm_actualparameters;
    }


    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }
    public List<astm_ActualParameter> getAstm_actualparameters() {
        return astm_actualparameters;
    }

    public void addAstm_actualparameter(Astm_actualparameter astm_actualparameter) {
        this.astm_actualparameters.add(astm_actualparameter);
    }

}