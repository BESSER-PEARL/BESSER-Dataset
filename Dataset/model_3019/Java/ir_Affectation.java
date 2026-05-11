





import java.util.List;
import java.util.ArrayList;

public class ir_Affectation extends Instruction {






    private ir_Expression ir_expression;




    private ir_ArgOrVarRef ir_argorvarref;


    public ir_Affectation(
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
    public ir_ArgOrVarRef getIr_argorvarref() {
        return ir_argorvarref;
    }

    public void setIr_argorvarref(ir_ArgOrVarRef ir_argorvarref) {
        this.ir_argorvarref = ir_argorvarref;
    }

}