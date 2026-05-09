





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_EncapsulatedClassifier extends StructuredClassifier {






    private List<UML2WithID_Port> uml2withid_ports;


    public UML2WithID_EncapsulatedClassifier(
    ) {
        super(
        );
        this.uml2withid_ports = new ArrayList<>();
    }

    public UML2WithID_EncapsulatedClassifier(
        ArrayList<UML2WithID_Port> uml2withid_ports    ) {
        this.uml2withid_ports = uml2withid_ports;
    }


    public List<UML2WithID_Port> getUml2withid_ports() {
        return uml2withid_ports;
    }

    public void addUml2withid_port(Uml2withid_port uml2withid_port) {
        this.uml2withid_ports.add(uml2withid_port);
    }

}