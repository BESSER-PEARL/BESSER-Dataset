





import java.util.List;
import java.util.ArrayList;

public class ir_LambdaExpression extends Scope, Expression {






    private List<ir_Variable> ir_variables;




    private ir_Expression ir_expression;


    public ir_LambdaExpression(
    ) {
        super(
        );
        this.ir_variables = new ArrayList<>();
    }

    public ir_LambdaExpression(
        ArrayList<ir_Variable> ir_variables    ) {
        this.ir_variables = ir_variables;
    }


    public List<ir_Variable> getIr_variables() {
        return ir_variables;
    }

    public void addIr_variable(Ir_variable ir_variable) {
        this.ir_variables.add(ir_variable);
    }
    public ir_Expression getIr_expression() {
        return ir_expression;
    }

    public void setIr_expression(ir_Expression ir_expression) {
        this.ir_expression = ir_expression;
    }

}