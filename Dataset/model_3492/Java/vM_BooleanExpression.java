





import java.util.List;
import java.util.ArrayList;

public class vM_BooleanExpression extends Expression {

    private String op;
    private String value;





    private vM_BooleanExpression vm_booleanexpression;


    public vM_BooleanExpression(
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

    public vM_BooleanExpression getVm_booleanexpression() {
        return vm_booleanexpression;
    }

    public void setVm_booleanexpression(vM_BooleanExpression vm_booleanexpression) {
        this.vm_booleanexpression = vm_booleanexpression;
    }

}