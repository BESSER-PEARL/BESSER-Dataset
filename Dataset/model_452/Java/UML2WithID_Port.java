





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Port extends Property {

    private boolean isBehavior;
    private boolean isService;





    private List<UML2WithID_Interface> uml2withid_interfaces;




    private List<UML2WithID_Interface> uml2withid_interfaces;




    private UML2WithID_Trigger uml2withid_trigger;




    private List<UML2WithID_Port> uml2withid_ports;


    public UML2WithID_Port(
        boolean isBehavior,        boolean isService    ) {
        super(
        );
        this.isBehavior = isBehavior;
        this.isService = isService;
        this.uml2withid_interfaces = new ArrayList<>();
        this.uml2withid_interfaces = new ArrayList<>();
        this.uml2withid_ports = new ArrayList<>();
    }

    public UML2WithID_Port(
        boolean isBehavior,        boolean isService        ArrayList<UML2WithID_Interface> uml2withid_interfaces,        ArrayList<UML2WithID_Interface> uml2withid_interfaces,        ArrayList<UML2WithID_Port> uml2withid_ports    ) {
        this.isBehavior = isBehavior;
        this.isService = isService;
        this.uml2withid_interfaces = uml2withid_interfaces;
        this.uml2withid_interfaces = uml2withid_interfaces;
        this.uml2withid_ports = uml2withid_ports;
    }

    public boolean getIsbehavior() {
        return isBehavior;
    }

    public void setIsbehavior(boolean isBehavior) {
        this.isBehavior = isBehavior;
    }
    public boolean getIsservice() {
        return isService;
    }

    public void setIsservice(boolean isService) {
        this.isService = isService;
    }

    public List<UML2WithID_Interface> getUml2withid_interfaces() {
        return uml2withid_interfaces;
    }

    public void addUml2withid_interface(Uml2withid_interface uml2withid_interface) {
        this.uml2withid_interfaces.add(uml2withid_interface);
    }
    public List<UML2WithID_Interface> getUml2withid_interfaces() {
        return uml2withid_interfaces;
    }

    public void addUml2withid_interface(Uml2withid_interface uml2withid_interface) {
        this.uml2withid_interfaces.add(uml2withid_interface);
    }
    public UML2WithID_Trigger getUml2withid_trigger() {
        return uml2withid_trigger;
    }

    public void setUml2withid_trigger(UML2WithID_Trigger uml2withid_trigger) {
        this.uml2withid_trigger = uml2withid_trigger;
    }
    public List<UML2WithID_Port> getUml2withid_ports() {
        return uml2withid_ports;
    }

    public void addUml2withid_port(Uml2withid_port uml2withid_port) {
        this.uml2withid_ports.add(uml2withid_port);
    }

}