





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Port extends Property {

    private String isBehavior;
    private String isService;





    private List<uml3_0_0_Port> uml3_0_0_ports;




    private uml3_0_0_ProtocolStateMachine uml3_0_0_protocolstatemachine;




    private List<uml3_0_0_Interface> uml3_0_0_interfaces;




    private List<uml3_0_0_Interface> uml3_0_0_interfaces;




    private uml3_0_0_Trigger uml3_0_0_trigger;


    public uml3_0_0_Port(
        String isBehavior,        String isService    ) {
        super(
        );
        this.isBehavior = isBehavior;
        this.isService = isService;
        this.uml3_0_0_ports = new ArrayList<>();
        this.uml3_0_0_interfaces = new ArrayList<>();
        this.uml3_0_0_interfaces = new ArrayList<>();
    }

    public uml3_0_0_Port(
        String isBehavior,        String isService        ArrayList<uml3_0_0_Port> uml3_0_0_ports,        ArrayList<uml3_0_0_Interface> uml3_0_0_interfaces,        ArrayList<uml3_0_0_Interface> uml3_0_0_interfaces    ) {
        this.isBehavior = isBehavior;
        this.isService = isService;
        this.uml3_0_0_ports = uml3_0_0_ports;
        this.uml3_0_0_interfaces = uml3_0_0_interfaces;
        this.uml3_0_0_interfaces = uml3_0_0_interfaces;
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

    public List<uml3_0_0_Port> getUml3_0_0_ports() {
        return uml3_0_0_ports;
    }

    public void addUml3_0_0_port(Uml3_0_0_port uml3_0_0_port) {
        this.uml3_0_0_ports.add(uml3_0_0_port);
    }
    public uml3_0_0_ProtocolStateMachine getUml3_0_0_protocolstatemachine() {
        return uml3_0_0_protocolstatemachine;
    }

    public void setUml3_0_0_protocolstatemachine(uml3_0_0_ProtocolStateMachine uml3_0_0_protocolstatemachine) {
        this.uml3_0_0_protocolstatemachine = uml3_0_0_protocolstatemachine;
    }
    public List<uml3_0_0_Interface> getUml3_0_0_interfaces() {
        return uml3_0_0_interfaces;
    }

    public void addUml3_0_0_interface(Uml3_0_0_interface uml3_0_0_interface) {
        this.uml3_0_0_interfaces.add(uml3_0_0_interface);
    }
    public List<uml3_0_0_Interface> getUml3_0_0_interfaces() {
        return uml3_0_0_interfaces;
    }

    public void addUml3_0_0_interface(Uml3_0_0_interface uml3_0_0_interface) {
        this.uml3_0_0_interfaces.add(uml3_0_0_interface);
    }
    public uml3_0_0_Trigger getUml3_0_0_trigger() {
        return uml3_0_0_trigger;
    }

    public void setUml3_0_0_trigger(uml3_0_0_Trigger uml3_0_0_trigger) {
        this.uml3_0_0_trigger = uml3_0_0_trigger;
    }

}