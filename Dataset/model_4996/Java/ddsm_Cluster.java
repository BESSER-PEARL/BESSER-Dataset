





import java.util.List;
import java.util.ArrayList;

public class ddsm_Cluster extends ExternalComponent {






    private List<ddsm_VM> ddsm_vms;


    public ddsm_Cluster(
    ) {
        super(
        );
        this.ddsm_vms = new ArrayList<>();
    }

    public ddsm_Cluster(
        ArrayList<ddsm_VM> ddsm_vms    ) {
        this.ddsm_vms = ddsm_vms;
    }


    public List<ddsm_VM> getDdsm_vms() {
        return ddsm_vms;
    }

    public void addDdsm_vm(Ddsm_vm ddsm_vm) {
        this.ddsm_vms.add(ddsm_vm);
    }

}