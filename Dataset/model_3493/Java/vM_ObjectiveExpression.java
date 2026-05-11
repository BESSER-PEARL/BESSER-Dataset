





import java.util.List;
import java.util.ArrayList;

public class vM_ObjectiveExpression  {

    private String op;





    private vM_PrimitiveExpression vm_primitiveexpression;




    private vM_Objective vm_objective;


    public vM_ObjectiveExpression(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public vM_PrimitiveExpression getVm_primitiveexpression() {
        return vm_primitiveexpression;
    }

    public void setVm_primitiveexpression(vM_PrimitiveExpression vm_primitiveexpression) {
        this.vm_primitiveexpression = vm_primitiveexpression;
    }
    public vM_Objective getVm_objective() {
        return vm_objective;
    }

    public void setVm_objective(vM_Objective vm_objective) {
        this.vm_objective = vm_objective;
    }

}