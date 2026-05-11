





import java.util.List;
import java.util.ArrayList;

public class ir_Assign extends Statement {






    private ir_Expression ir_expression;




    private ir_VariableReference ir_variablereference;


    public ir_Assign(
    ) {
        super(
        );
    }



    public ir_Expression getIr_expression() {
        return ir_expression;
    }

    public void setIr_expression(ir_Expression ir_expression) {
        this.ir_expression = ir_expression;
    }
    public ir_VariableReference getIr_variablereference() {
        return ir_variablereference;
    }

    public void setIr_variablereference(ir_VariableReference ir_variablereference) {
        this.ir_variablereference = ir_variablereference;
    }

}