





import java.util.List;
import java.util.ArrayList;

public class vM_SpecialExpression extends Expression {

    private String op;





    private vM_Feature vm_feature;


    public vM_SpecialExpression(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public vM_Feature getVm_feature() {
        return vm_feature;
    }

    public void setVm_feature(vM_Feature vm_feature) {
        this.vm_feature = vm_feature;
    }

}