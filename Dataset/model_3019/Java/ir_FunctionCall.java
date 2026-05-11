





import java.util.List;
import java.util.ArrayList;

public class ir_FunctionCall extends Expression {






    private ir_Function ir_function;




    private List<ir_Expression> ir_expressions;


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


    public ir_Function getIr_function() {
        return ir_function;
    }

    public void setIr_function(ir_Function ir_function) {
        this.ir_function = ir_function;
    }
    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }

}