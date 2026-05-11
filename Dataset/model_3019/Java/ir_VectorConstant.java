





import java.util.List;
import java.util.ArrayList;

public class ir_VectorConstant extends Expression {






    private List<ir_Expression> ir_expressions;


    public ir_VectorConstant(
    ) {
        super(
        );
        this.ir_expressions = new ArrayList<>();
    }

    public ir_VectorConstant(
        ArrayList<ir_Expression> ir_expressions    ) {
        this.ir_expressions = ir_expressions;
    }


    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }

}