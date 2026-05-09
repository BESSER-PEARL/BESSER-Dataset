





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ProtocolStateMachine extends StateMachine {






    private List<UMLModel_ProtocolConformance> umlmodel_protocolconformances;




    private UMLModel_Interface umlmodel_interface;


    public UMLModel_ProtocolStateMachine(
    ) {
        super(
        );
        this.umlmodel_protocolconformances = new ArrayList<>();
    }

    public UMLModel_ProtocolStateMachine(
        ArrayList<UMLModel_ProtocolConformance> umlmodel_protocolconformances    ) {
        this.umlmodel_protocolconformances = umlmodel_protocolconformances;
    }


    public List<UMLModel_ProtocolConformance> getUmlmodel_protocolconformances() {
        return umlmodel_protocolconformances;
    }

    public void addUmlmodel_protocolconformance(Umlmodel_protocolconformance umlmodel_protocolconformance) {
        this.umlmodel_protocolconformances.add(umlmodel_protocolconformance);
    }
    public UMLModel_Interface getUmlmodel_interface() {
        return umlmodel_interface;
    }

    public void setUmlmodel_interface(UMLModel_Interface umlmodel_interface) {
        this.umlmodel_interface = umlmodel_interface;
    }

}