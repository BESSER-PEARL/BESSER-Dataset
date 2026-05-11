





import java.util.List;
import java.util.ArrayList;

public class vM_Configuration  {

    private String name;





    private vM_Configurations vm_configurations;




    private List<vM_BooleanValuation> vm_booleanvaluations;




    private List<vM_ExtendedValuation> vm_extendedvaluations;


    public vM_Configuration(
        String name    ) {
        this.name = name;
        this.vm_booleanvaluations = new ArrayList<>();
        this.vm_extendedvaluations = new ArrayList<>();
    }

    public vM_Configuration(
        String name        ArrayList<vM_BooleanValuation> vm_booleanvaluations,        ArrayList<vM_ExtendedValuation> vm_extendedvaluations    ) {
        this.name = name;
        this.vm_booleanvaluations = vm_booleanvaluations;
        this.vm_extendedvaluations = vm_extendedvaluations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vM_Configurations getVm_configurations() {
        return vm_configurations;
    }

    public void setVm_configurations(vM_Configurations vm_configurations) {
        this.vm_configurations = vm_configurations;
    }
    public List<vM_BooleanValuation> getVm_booleanvaluations() {
        return vm_booleanvaluations;
    }

    public void addVm_booleanvaluation(Vm_booleanvaluation vm_booleanvaluation) {
        this.vm_booleanvaluations.add(vm_booleanvaluation);
    }
    public List<vM_ExtendedValuation> getVm_extendedvaluations() {
        return vm_extendedvaluations;
    }

    public void addVm_extendedvaluation(Vm_extendedvaluation vm_extendedvaluation) {
        this.vm_extendedvaluations.add(vm_extendedvaluation);
    }

}