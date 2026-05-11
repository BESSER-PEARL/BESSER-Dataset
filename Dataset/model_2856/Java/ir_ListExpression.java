





import java.util.List;
import java.util.ArrayList;

public class ir_ListExpression extends Expression {






    private List<ir_Generator> ir_generators;




    private List<ir_Expression> ir_expressions;


    public ir_ListExpression(
    ) {
        super(
        );
        this.ir_generators = new ArrayList<>();
        this.ir_expressions = new ArrayList<>();
    }

    public ir_ListExpression(
        ArrayList<ir_Generator> ir_generators,        ArrayList<ir_Expression> ir_expressions    ) {
        this.ir_generators = ir_generators;
        this.ir_expressions = ir_expressions;
    }


    public List<ir_Generator> getIr_generators() {
        return ir_generators;
    }

    public void addIr_generator(Ir_generator ir_generator) {
        this.ir_generators.add(ir_generator);
    }
    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }

}