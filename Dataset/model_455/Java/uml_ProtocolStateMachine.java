





import java.util.List;
import java.util.ArrayList;

public class uml_ProtocolStateMachine extends StateMachine {






    private List<uml_ProtocolConformance> uml_protocolconformances;




    private uml_ProtocolConformance uml_protocolconformance;




    private uml_ProtocolConformance uml_protocolconformance;




    private uml_Interface uml_interface;


    public uml_ProtocolStateMachine(
    ) {
        super(
        );
        this.uml_protocolconformances = new ArrayList<>();
    }

    public uml_ProtocolStateMachine(
        ArrayList<uml_ProtocolConformance> uml_protocolconformances    ) {
        this.uml_protocolconformances = uml_protocolconformances;
    }


    public List<uml_ProtocolConformance> getUml_protocolconformances() {
        return uml_protocolconformances;
    }

    public void addUml_protocolconformance(Uml_protocolconformance uml_protocolconformance) {
        this.uml_protocolconformances.add(uml_protocolconformance);
    }
    public uml_ProtocolConformance getUml_protocolconformance() {
        return uml_protocolconformance;
    }

    public void setUml_protocolconformance(uml_ProtocolConformance uml_protocolconformance) {
        this.uml_protocolconformance = uml_protocolconformance;
    }
    public uml_ProtocolConformance getUml_protocolconformance() {
        return uml_protocolconformance;
    }

    public void setUml_protocolconformance(uml_ProtocolConformance uml_protocolconformance) {
        this.uml_protocolconformance = uml_protocolconformance;
    }
    public uml_Interface getUml_interface() {
        return uml_interface;
    }

    public void setUml_interface(uml_Interface uml_interface) {
        this.uml_interface = uml_interface;
    }

}