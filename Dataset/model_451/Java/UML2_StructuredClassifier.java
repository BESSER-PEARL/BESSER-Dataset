





import java.util.List;
import java.util.ArrayList;

public class UML2_StructuredClassifier extends Classifier {






    private List<UML2_Connector> uml2_connectors;




    private List<UML2_ConnectableElement> uml2_connectableelements;


    public UML2_StructuredClassifier(
    ) {
        super(
        );
        this.uml2_connectors = new ArrayList<>();
        this.uml2_connectableelements = new ArrayList<>();
    }

    public UML2_StructuredClassifier(
        ArrayList<UML2_Connector> uml2_connectors,        ArrayList<UML2_ConnectableElement> uml2_connectableelements    ) {
        this.uml2_connectors = uml2_connectors;
        this.uml2_connectableelements = uml2_connectableelements;
    }


    public List<UML2_Connector> getUml2_connectors() {
        return uml2_connectors;
    }

    public void addUml2_connector(Uml2_connector uml2_connector) {
        this.uml2_connectors.add(uml2_connector);
    }
    public List<UML2_ConnectableElement> getUml2_connectableelements() {
        return uml2_connectableelements;
    }

    public void addUml2_connectableelement(Uml2_connectableelement uml2_connectableelement) {
        this.uml2_connectableelements.add(uml2_connectableelement);
    }

}