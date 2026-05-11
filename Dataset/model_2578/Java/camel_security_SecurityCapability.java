





import java.util.List;
import java.util.ArrayList;

public class camel_security_SecurityCapability  {

    private String name;





    private List<SecurityControl> securitycontrols;




    private DataCenter datacenter;


    public camel_security_SecurityCapability(
        String name    ) {
        this.name = name;
        this.securitycontrols = new ArrayList<>();
    }

    public camel_security_SecurityCapability(
        String name        ArrayList<SecurityControl> securitycontrols    ) {
        this.name = name;
        this.securitycontrols = securitycontrols;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<SecurityControl> getSecuritycontrols() {
        return securitycontrols;
    }

    public void addSecuritycontrol(Securitycontrol securitycontrol) {
        this.securitycontrols.add(securitycontrol);
    }
    public DataCenter getDatacenter() {
        return datacenter;
    }

    public void setDatacenter(DataCenter datacenter) {
        this.datacenter = datacenter;
    }

}