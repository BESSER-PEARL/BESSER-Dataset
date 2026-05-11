





import java.util.List;
import java.util.ArrayList;

public class vM_NumericExpression extends Expression {

    private String op;
    private String value;





    private vM_NumericExpression vm_numericexpression;


    public vM_NumericExpression(
        String op,        String value    ) {
        super(
        );
        this.op = op;
        this.value = value;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public vM_NumericExpression getVm_numericexpression() {
        return vm_numericexpression;
    }

    public void setVm_numericexpression(vM_NumericExpression vm_numericexpression) {
        this.vm_numericexpression = vm_numericexpression;
    }

}