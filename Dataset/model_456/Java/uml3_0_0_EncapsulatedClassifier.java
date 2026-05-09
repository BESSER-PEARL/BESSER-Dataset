





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_EncapsulatedClassifier extends StructuredClassifier {






    private List<uml3_0_0_Port> uml3_0_0_ports;


    public uml3_0_0_EncapsulatedClassifier(
    ) {
        super(
        );
        this.uml3_0_0_ports = new ArrayList<>();
    }

    public uml3_0_0_EncapsulatedClassifier(
        ArrayList<uml3_0_0_Port> uml3_0_0_ports    ) {
        this.uml3_0_0_ports = uml3_0_0_ports;
    }


    public List<uml3_0_0_Port> getUml3_0_0_ports() {
        return uml3_0_0_ports;
    }

    public void addUml3_0_0_port(Uml3_0_0_port uml3_0_0_port) {
        this.uml3_0_0_ports.add(uml3_0_0_port);
    }

}