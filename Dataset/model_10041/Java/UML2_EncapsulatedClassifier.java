





import java.util.List;
import java.util.ArrayList;

public class UML2_EncapsulatedClassifier extends StructuredClassifier {






    private List<UML2_Port> uml2_ports;


    public UML2_EncapsulatedClassifier(
    ) {
        super(
        );
        this.uml2_ports = new ArrayList<>();
    }

    public UML2_EncapsulatedClassifier(
        ArrayList<UML2_Port> uml2_ports    ) {
        this.uml2_ports = uml2_ports;
    }


    public List<UML2_Port> getUml2_ports() {
        return uml2_ports;
    }

    public void addUml2_port(Uml2_port uml2_port) {
        this.uml2_ports.add(uml2_port);
    }

}