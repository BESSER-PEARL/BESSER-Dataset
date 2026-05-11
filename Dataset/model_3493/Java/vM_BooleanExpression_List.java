





import java.util.List;
import java.util.ArrayList;

public class vM_BooleanExpression_List  {






    private vM_BooleanExpression vm_booleanexpression;




    private List<vM_BooleanExpression> vm_booleanexpressions;


    public vM_BooleanExpression_List(
    ) {
        this.vm_booleanexpressions = new ArrayList<>();
    }

    public vM_BooleanExpression_List(
        ArrayList<vM_BooleanExpression> vm_booleanexpressions    ) {
        this.vm_booleanexpressions = vm_booleanexpressions;
    }


    public vM_BooleanExpression getVm_booleanexpression() {
        return vm_booleanexpression;
    }

    public void setVm_booleanexpression(vM_BooleanExpression vm_booleanexpression) {
        this.vm_booleanexpression = vm_booleanexpression;
    }
    public List<vM_BooleanExpression> getVm_booleanexpressions() {
        return vm_booleanexpressions;
    }

    public void addVm_booleanexpression(Vm_booleanexpression vm_booleanexpression) {
        this.vm_booleanexpressions.add(vm_booleanexpression);
    }

}