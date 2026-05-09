





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ProtocolStateMachine extends StateMachine {






    private uml3_0_0_ProtocolConformance uml3_0_0_protocolconformance;




    private uml3_0_0_Interface uml3_0_0_interface;




    private List<uml3_0_0_ProtocolConformance> uml3_0_0_protocolconformances;




    private uml3_0_0_ProtocolConformance uml3_0_0_protocolconformance;


    public uml3_0_0_ProtocolStateMachine(
    ) {
        super(
        );
        this.uml3_0_0_protocolconformances = new ArrayList<>();
    }

    public uml3_0_0_ProtocolStateMachine(
        ArrayList<uml3_0_0_ProtocolConformance> uml3_0_0_protocolconformances    ) {
        this.uml3_0_0_protocolconformances = uml3_0_0_protocolconformances;
    }


    public uml3_0_0_ProtocolConformance getUml3_0_0_protocolconformance() {
        return uml3_0_0_protocolconformance;
    }

    public void setUml3_0_0_protocolconformance(uml3_0_0_ProtocolConformance uml3_0_0_protocolconformance) {
        this.uml3_0_0_protocolconformance = uml3_0_0_protocolconformance;
    }
    public uml3_0_0_Interface getUml3_0_0_interface() {
        return uml3_0_0_interface;
    }

    public void setUml3_0_0_interface(uml3_0_0_Interface uml3_0_0_interface) {
        this.uml3_0_0_interface = uml3_0_0_interface;
    }
    public List<uml3_0_0_ProtocolConformance> getUml3_0_0_protocolconformances() {
        return uml3_0_0_protocolconformances;
    }

    public void addUml3_0_0_protocolconformance(Uml3_0_0_protocolconformance uml3_0_0_protocolconformance) {
        this.uml3_0_0_protocolconformances.add(uml3_0_0_protocolconformance);
    }
    public uml3_0_0_ProtocolConformance getUml3_0_0_protocolconformance() {
        return uml3_0_0_protocolconformance;
    }

    public void setUml3_0_0_protocolconformance(uml3_0_0_ProtocolConformance uml3_0_0_protocolconformance) {
        this.uml3_0_0_protocolconformance = uml3_0_0_protocolconformance;
    }

}