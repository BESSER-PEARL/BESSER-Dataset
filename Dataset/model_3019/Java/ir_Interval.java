





import java.util.List;
import java.util.ArrayList;

public class ir_Interval extends IterationBlock {






    private ir_Expression ir_expression;




    private ir_SimpleVariable ir_simplevariable;


    public ir_Interval(
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
    public ir_SimpleVariable getIr_simplevariable() {
        return ir_simplevariable;
    }

    public void setIr_simplevariable(ir_SimpleVariable ir_simplevariable) {
        this.ir_simplevariable = ir_simplevariable;
    }

}