





import java.util.List;
import java.util.ArrayList;

public class vM_If extends ComplexExpression {






    private List<vM_ComplexExpression> vm_complexexpressions;




    private vM_ComplexExpression vm_complexexpression;


    public vM_If(
    ) {
        super(
        );
        this.vm_complexexpressions = new ArrayList<>();
    }

    public vM_If(
        ArrayList<vM_ComplexExpression> vm_complexexpressions    ) {
        this.vm_complexexpressions = vm_complexexpressions;
    }


    public List<vM_ComplexExpression> getVm_complexexpressions() {
        return vm_complexexpressions;
    }

    public void addVm_complexexpression(Vm_complexexpression vm_complexexpression) {
        this.vm_complexexpressions.add(vm_complexexpression);
    }
    public vM_ComplexExpression getVm_complexexpression() {
        return vm_complexexpression;
    }

    public void setVm_complexexpression(vM_ComplexExpression vm_complexexpression) {
        this.vm_complexexpression = vm_complexexpression;
    }

}