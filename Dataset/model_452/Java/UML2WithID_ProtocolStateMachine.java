





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ProtocolStateMachine extends StateMachine {






    private UML2WithID_ProtocolConformance uml2withid_protocolconformance;




    private UML2WithID_ProtocolConformance uml2withid_protocolconformance;




    private UML2WithID_Interface uml2withid_interface;




    private List<UML2WithID_ProtocolConformance> uml2withid_protocolconformances;




    private UML2WithID_Port uml2withid_port;


    public UML2WithID_ProtocolStateMachine(
    ) {
        super(
        );
        this.uml2withid_protocolconformances = new ArrayList<>();
    }

    public UML2WithID_ProtocolStateMachine(
        ArrayList<UML2WithID_ProtocolConformance> uml2withid_protocolconformances    ) {
        this.uml2withid_protocolconformances = uml2withid_protocolconformances;
    }


    public UML2WithID_ProtocolConformance getUml2withid_protocolconformance() {
        return uml2withid_protocolconformance;
    }

    public void setUml2withid_protocolconformance(UML2WithID_ProtocolConformance uml2withid_protocolconformance) {
        this.uml2withid_protocolconformance = uml2withid_protocolconformance;
    }
    public UML2WithID_ProtocolConformance getUml2withid_protocolconformance() {
        return uml2withid_protocolconformance;
    }

    public void setUml2withid_protocolconformance(UML2WithID_ProtocolConformance uml2withid_protocolconformance) {
        this.uml2withid_protocolconformance = uml2withid_protocolconformance;
    }
    public UML2WithID_Interface getUml2withid_interface() {
        return uml2withid_interface;
    }

    public void setUml2withid_interface(UML2WithID_Interface uml2withid_interface) {
        this.uml2withid_interface = uml2withid_interface;
    }
    public List<UML2WithID_ProtocolConformance> getUml2withid_protocolconformances() {
        return uml2withid_protocolconformances;
    }

    public void addUml2withid_protocolconformance(Uml2withid_protocolconformance uml2withid_protocolconformance) {
        this.uml2withid_protocolconformances.add(uml2withid_protocolconformance);
    }
    public UML2WithID_Port getUml2withid_port() {
        return uml2withid_port;
    }

    public void setUml2withid_port(UML2WithID_Port uml2withid_port) {
        this.uml2withid_port = uml2withid_port;
    }

}