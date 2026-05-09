





import java.util.List;
import java.util.ArrayList;

public class UML2_Interface extends Classifier {






    private UML2_Component uml2_component;




    private UML2_Port uml2_port;




    private List<UML2_Operation> uml2_operations;




    private UML2_Port uml2_port;




    private UML2_Implementation uml2_implementation;




    private UML2_Interface uml2_interface;




    private UML2_ProtocolStateMachine uml2_protocolstatemachine;




    private List<UML2_Reception> uml2_receptions;




    private UML2_Component uml2_component;


    public UML2_Interface(
    ) {
        super(
        );
        this.uml2_operations = new ArrayList<>();
        this.uml2_receptions = new ArrayList<>();
    }

    public UML2_Interface(
        ArrayList<UML2_Operation> uml2_operations,        ArrayList<UML2_Reception> uml2_receptions    ) {
        this.uml2_operations = uml2_operations;
        this.uml2_receptions = uml2_receptions;
    }


    public UML2_Component getUml2_component() {
        return uml2_component;
    }

    public void setUml2_component(UML2_Component uml2_component) {
        this.uml2_component = uml2_component;
    }
    public UML2_Port getUml2_port() {
        return uml2_port;
    }

    public void setUml2_port(UML2_Port uml2_port) {
        this.uml2_port = uml2_port;
    }
    public List<UML2_Operation> getUml2_operations() {
        return uml2_operations;
    }

    public void addUml2_operation(Uml2_operation uml2_operation) {
        this.uml2_operations.add(uml2_operation);
    }
    public UML2_Port getUml2_port() {
        return uml2_port;
    }

    public void setUml2_port(UML2_Port uml2_port) {
        this.uml2_port = uml2_port;
    }
    public UML2_Implementation getUml2_implementation() {
        return uml2_implementation;
    }

    public void setUml2_implementation(UML2_Implementation uml2_implementation) {
        this.uml2_implementation = uml2_implementation;
    }
    public UML2_Interface getUml2_interface() {
        return uml2_interface;
    }

    public void setUml2_interface(UML2_Interface uml2_interface) {
        this.uml2_interface = uml2_interface;
    }
    public UML2_ProtocolStateMachine getUml2_protocolstatemachine() {
        return uml2_protocolstatemachine;
    }

    public void setUml2_protocolstatemachine(UML2_ProtocolStateMachine uml2_protocolstatemachine) {
        this.uml2_protocolstatemachine = uml2_protocolstatemachine;
    }
    public List<UML2_Reception> getUml2_receptions() {
        return uml2_receptions;
    }

    public void addUml2_reception(Uml2_reception uml2_reception) {
        this.uml2_receptions.add(uml2_reception);
    }
    public UML2_Component getUml2_component() {
        return uml2_component;
    }

    public void setUml2_component(UML2_Component uml2_component) {
        this.uml2_component = uml2_component;
    }

}