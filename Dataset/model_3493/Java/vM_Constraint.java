





import java.util.List;
import java.util.ArrayList;

public class vM_Constraint  {

    private String name;





    private vM_Constraints vm_constraints;


    public vM_Constraint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vM_Constraints getVm_constraints() {
        return vm_constraints;
    }

    public void setVm_constraints(vM_Constraints vm_constraints) {
        this.vm_constraints = vm_constraints;
    }

}