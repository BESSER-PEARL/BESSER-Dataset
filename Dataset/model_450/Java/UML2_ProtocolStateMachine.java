





import java.util.List;
import java.util.ArrayList;

public class UML2_ProtocolStateMachine extends StateMachine {






    private UML2_Interface uml2_interface;




    private UML2_Port uml2_port;




    private List<UML2_ProtocolConformance> uml2_protocolconformances;




    private UML2_ProtocolConformance uml2_protocolconformance;




    private UML2_ProtocolConformance uml2_protocolconformance;


    public UML2_ProtocolStateMachine(
    ) {
        super(
        );
        this.uml2_protocolconformances = new ArrayList<>();
    }

    public UML2_ProtocolStateMachine(
        ArrayList<UML2_ProtocolConformance> uml2_protocolconformances    ) {
        this.uml2_protocolconformances = uml2_protocolconformances;
    }


    public UML2_Interface getUml2_interface() {
        return uml2_interface;
    }

    public void setUml2_interface(UML2_Interface uml2_interface) {
        this.uml2_interface = uml2_interface;
    }
    public UML2_Port getUml2_port() {
        return uml2_port;
    }

    public void setUml2_port(UML2_Port uml2_port) {
        this.uml2_port = uml2_port;
    }
    public List<UML2_ProtocolConformance> getUml2_protocolconformances() {
        return uml2_protocolconformances;
    }

    public void addUml2_protocolconformance(Uml2_protocolconformance uml2_protocolconformance) {
        this.uml2_protocolconformances.add(uml2_protocolconformance);
    }
    public UML2_ProtocolConformance getUml2_protocolconformance() {
        return uml2_protocolconformance;
    }

    public void setUml2_protocolconformance(UML2_ProtocolConformance uml2_protocolconformance) {
        this.uml2_protocolconformance = uml2_protocolconformance;
    }
    public UML2_ProtocolConformance getUml2_protocolconformance() {
        return uml2_protocolconformance;
    }

    public void setUml2_protocolconformance(UML2_ProtocolConformance uml2_protocolconformance) {
        this.uml2_protocolconformance = uml2_protocolconformance;
    }

}