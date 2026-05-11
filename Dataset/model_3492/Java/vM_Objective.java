





import java.util.List;
import java.util.ArrayList;

public class vM_Objective  {

    private String op;
    private String name;





    private vM_Objectives vm_objectives;


    public vM_Objective(
        String op,        String name    ) {
        this.op = op;
        this.name = name;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vM_Objectives getVm_objectives() {
        return vm_objectives;
    }

    public void setVm_objectives(vM_Objectives vm_objectives) {
        this.vm_objectives = vm_objectives;
    }

}