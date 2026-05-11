





import java.util.List;
import java.util.ArrayList;

public class ir_Variable extends Declaration {

    private boolean parameter;
    private boolean constant;





    private ir_AbstractActor ir_abstractactor;


    public ir_Variable(
        boolean parameter,        boolean constant    ) {
        super(
        );
        this.parameter = parameter;
        this.constant = constant;
    }


    public boolean getParameter() {
        return parameter;
    }

    public void setParameter(boolean parameter) {
        this.parameter = parameter;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }

    public ir_AbstractActor getIr_abstractactor() {
        return ir_abstractactor;
    }

    public void setIr_abstractactor(ir_AbstractActor ir_abstractactor) {
        this.ir_abstractactor = ir_abstractactor;
    }

}