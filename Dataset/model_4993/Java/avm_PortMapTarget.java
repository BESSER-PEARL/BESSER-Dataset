





import java.util.List;
import java.util.ArrayList;

public class avm_PortMapTarget  {

    private String ID;





    private List<avm_PortMapTarget> avm_portmaptargets;


    public avm_PortMapTarget(
        String ID    ) {
        this.ID = ID;
        this.avm_portmaptargets = new ArrayList<>();
    }

    public avm_PortMapTarget(
        String ID        ArrayList<avm_PortMapTarget> avm_portmaptargets    ) {
        this.ID = ID;
        this.avm_portmaptargets = avm_portmaptargets;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<avm_PortMapTarget> getAvm_portmaptargets() {
        return avm_portmaptargets;
    }

    public void addAvm_portmaptarget(Avm_portmaptarget avm_portmaptarget) {
        this.avm_portmaptargets.add(avm_portmaptarget);
    }

}