





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Cloud extends CloudMLElementWithProperties {






    private List<VMInstance> vminstances;


    public cloudml_core_Cloud(
    ) {
        super(
        );
        this.vminstances = new ArrayList<>();
    }

    public cloudml_core_Cloud(
        ArrayList<VMInstance> vminstances    ) {
        this.vminstances = vminstances;
    }


    public List<VMInstance> getVminstances() {
        return vminstances;
    }

    public void addVminstance(Vminstance vminstance) {
        this.vminstances.add(vminstance);
    }

}