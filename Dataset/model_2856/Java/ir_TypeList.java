





import java.util.List;
import java.util.ArrayList;

public class ir_TypeList extends Type {






    private ir_Type ir_type;




    private ir_Expression ir_expression;


    public ir_TypeList(
    ) {
        super(
        );
    }



    public ir_Type getIr_type() {
        return ir_type;
    }

    public void setIr_type(ir_Type ir_type) {
        this.ir_type = ir_type;
    }
    public ir_Expression getIr_expression() {
        return ir_expression;
    }

    public void setIr_expression(ir_Expression ir_expression) {
        this.ir_expression = ir_expression;
    }

}