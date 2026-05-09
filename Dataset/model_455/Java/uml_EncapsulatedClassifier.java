





import java.util.List;
import java.util.ArrayList;

public class uml_EncapsulatedClassifier extends StructuredClassifier {






    private List<uml_Port> uml_ports;


    public uml_EncapsulatedClassifier(
    ) {
        super(
        );
        this.uml_ports = new ArrayList<>();
    }

    public uml_EncapsulatedClassifier(
        ArrayList<uml_Port> uml_ports    ) {
        this.uml_ports = uml_ports;
    }


    public List<uml_Port> getUml_ports() {
        return uml_ports;
    }

    public void addUml_port(Uml_port uml_port) {
        this.uml_ports.add(uml_port);
    }

}