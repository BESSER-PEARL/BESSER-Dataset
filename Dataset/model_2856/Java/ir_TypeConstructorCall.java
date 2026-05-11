





import java.util.List;
import java.util.ArrayList;

public class ir_TypeConstructorCall extends ExpressionCall {

    private String name;





    private List<ir_Expression> ir_expressions;




    private ir_Declaration ir_declaration;


    public ir_TypeConstructorCall(
        String name    ) {
        super(
        );
        this.name = name;
        this.ir_expressions = new ArrayList<>();
    }

    public ir_TypeConstructorCall(
        String name        ArrayList<ir_Expression> ir_expressions    ) {
        this.name = name;
        this.ir_expressions = ir_expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }
    public ir_Declaration getIr_declaration() {
        return ir_declaration;
    }

    public void setIr_declaration(ir_Declaration ir_declaration) {
        this.ir_declaration = ir_declaration;
    }

}