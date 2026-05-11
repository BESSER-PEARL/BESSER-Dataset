





import java.util.List;
import java.util.ArrayList;

public class avm_PortMapTarget  {

    private String ID;





    private avm_PortMapTarget avm_portmaptarget;


    public avm_PortMapTarget(
        String ID    ) {
        this.ID = ID;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public avm_PortMapTarget getAvm_portmaptarget() {
        return avm_portmaptarget;
    }

    public void setAvm_portmaptarget(avm_PortMapTarget avm_portmaptarget) {
        this.avm_portmaptarget = avm_portmaptarget;
    }

}