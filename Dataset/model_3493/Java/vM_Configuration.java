





import java.util.List;
import java.util.ArrayList;

public class vM_Configuration  {

    private String name;





    private vM_Configurations vm_configurations;


    public vM_Configuration(
        String name    ) {
        this.name = name;
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

}