





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_ExternalComponentInstance extends ComponentInstance {

    private String ips;





    private List<VMPortInstance> vmportinstances;


    public cloudml_core_ExternalComponentInstance(
        String ips    ) {
        super(
        );
        this.ips = ips;
        this.vmportinstances = new ArrayList<>();
    }

    public cloudml_core_ExternalComponentInstance(
        String ips        ArrayList<VMPortInstance> vmportinstances    ) {
        this.ips = ips;
        this.vmportinstances = vmportinstances;
    }

    public String getIps() {
        return ips;
    }

    public void setIps(String ips) {
        this.ips = ips;
    }

    public List<VMPortInstance> getVmportinstances() {
        return vmportinstances;
    }

    public void addVmportinstance(Vmportinstance vmportinstance) {
        this.vmportinstances.add(vmportinstance);
    }

}