





import java.util.List;
import java.util.ArrayList;

public class UML2_Port extends Property {

    private boolean isService;
    private boolean isBehavior;





    private List<UML2_Interface> uml2_interfaces;




    private UML2_Port uml2_port;




    private List<UML2_Interface> uml2_interfaces;




    private UML2_Trigger uml2_trigger;


    public UML2_Port(
        boolean isService,        boolean isBehavior    ) {
        super(
        );
        this.isService = isService;
        this.isBehavior = isBehavior;
        this.uml2_interfaces = new ArrayList<>();
        this.uml2_interfaces = new ArrayList<>();
    }

    public UML2_Port(
        boolean isService,        boolean isBehavior        ArrayList<UML2_Interface> uml2_interfaces,        ArrayList<UML2_Interface> uml2_interfaces    ) {
        this.isService = isService;
        this.isBehavior = isBehavior;
        this.uml2_interfaces = uml2_interfaces;
        this.uml2_interfaces = uml2_interfaces;
    }

    public boolean getIsservice() {
        return isService;
    }

    public void setIsservice(boolean isService) {
        this.isService = isService;
    }
    public boolean getIsbehavior() {
        return isBehavior;
    }

    public void setIsbehavior(boolean isBehavior) {
        this.isBehavior = isBehavior;
    }

    public List<UML2_Interface> getUml2_interfaces() {
        return uml2_interfaces;
    }

    public void addUml2_interface(Uml2_interface uml2_interface) {
        this.uml2_interfaces.add(uml2_interface);
    }
    public UML2_Port getUml2_port() {
        return uml2_port;
    }

    public void setUml2_port(UML2_Port uml2_port) {
        this.uml2_port = uml2_port;
    }
    public List<UML2_Interface> getUml2_interfaces() {
        return uml2_interfaces;
    }

    public void addUml2_interface(Uml2_interface uml2_interface) {
        this.uml2_interfaces.add(uml2_interface);
    }
    public UML2_Trigger getUml2_trigger() {
        return uml2_trigger;
    }

    public void setUml2_trigger(UML2_Trigger uml2_trigger) {
        this.uml2_trigger = uml2_trigger;
    }

}