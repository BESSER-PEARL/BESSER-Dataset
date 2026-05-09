





import java.util.List;
import java.util.ArrayList;

public class uml_Port extends Property {

    private String isBehavior;
    private String isService;





    private uml_Trigger uml_trigger;




    private List<uml_Interface> uml_interfaces;




    private uml_ProtocolStateMachine uml_protocolstatemachine;




    private List<uml_Interface> uml_interfaces;




    private uml_Port uml_port;


    public uml_Port(
        String isBehavior,        String isService    ) {
        super(
        );
        this.isBehavior = isBehavior;
        this.isService = isService;
        this.uml_interfaces = new ArrayList<>();
        this.uml_interfaces = new ArrayList<>();
    }

    public uml_Port(
        String isBehavior,        String isService        ArrayList<uml_Interface> uml_interfaces,        ArrayList<uml_Interface> uml_interfaces    ) {
        this.isBehavior = isBehavior;
        this.isService = isService;
        this.uml_interfaces = uml_interfaces;
        this.uml_interfaces = uml_interfaces;
    }

    public String getIsbehavior() {
        return isBehavior;
    }

    public void setIsbehavior(String isBehavior) {
        this.isBehavior = isBehavior;
    }
    public String getIsservice() {
        return isService;
    }

    public void setIsservice(String isService) {
        this.isService = isService;
    }

    public uml_Trigger getUml_trigger() {
        return uml_trigger;
    }

    public void setUml_trigger(uml_Trigger uml_trigger) {
        this.uml_trigger = uml_trigger;
    }
    public List<uml_Interface> getUml_interfaces() {
        return uml_interfaces;
    }

    public void addUml_interface(Uml_interface uml_interface) {
        this.uml_interfaces.add(uml_interface);
    }
    public uml_ProtocolStateMachine getUml_protocolstatemachine() {
        return uml_protocolstatemachine;
    }

    public void setUml_protocolstatemachine(uml_ProtocolStateMachine uml_protocolstatemachine) {
        this.uml_protocolstatemachine = uml_protocolstatemachine;
    }
    public List<uml_Interface> getUml_interfaces() {
        return uml_interfaces;
    }

    public void addUml_interface(Uml_interface uml_interface) {
        this.uml_interfaces.add(uml_interface);
    }
    public uml_Port getUml_port() {
        return uml_port;
    }

    public void setUml_port(uml_Port uml_port) {
        this.uml_port = uml_port;
    }

}