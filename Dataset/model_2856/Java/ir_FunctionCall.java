





import java.util.List;
import java.util.ArrayList;

public class ir_FunctionCall extends ExpressionCall {






    private List<ir_Expression> ir_expressions;




    private ir_Expression ir_expression;


    public ir_FunctionCall(
    ) {
        super(
        );
        this.ir_expressions = new ArrayList<>();
    }

    public ir_FunctionCall(
        ArrayList<ir_Expression> ir_expressions    ) {
        this.ir_expressions = ir_expressions;
    }


    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }
    public ir_Expression getIr_expression() {
        return ir_expression;
    }

    public void setIr_expression(ir_Expression ir_expression) {
        this.ir_expression = ir_expression;
    }

}