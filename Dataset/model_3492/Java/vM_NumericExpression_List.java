





import java.util.List;
import java.util.ArrayList;

public class vM_NumericExpression_List  {






    private vM_NumericExpression vm_numericexpression;




    private List<vM_NumericExpression> vm_numericexpressions;


    public vM_NumericExpression_List(
    ) {
        this.vm_numericexpressions = new ArrayList<>();
    }

    public vM_NumericExpression_List(
        ArrayList<vM_NumericExpression> vm_numericexpressions    ) {
        this.vm_numericexpressions = vm_numericexpressions;
    }


    public vM_NumericExpression getVm_numericexpression() {
        return vm_numericexpression;
    }

    public void setVm_numericexpression(vM_NumericExpression vm_numericexpression) {
        this.vm_numericexpression = vm_numericexpression;
    }
    public List<vM_NumericExpression> getVm_numericexpressions() {
        return vm_numericexpressions;
    }

    public void addVm_numericexpression(Vm_numericexpression vm_numericexpression) {
        this.vm_numericexpressions.add(vm_numericexpression);
    }

}