





import java.util.List;
import java.util.ArrayList;

public class UML2_ConnectableElement extends NamedElement, ParameterableElement {






    private UML2_StructuredClassifier uml2_structuredclassifier;




    private UML2_ConnectorEnd uml2_connectorend;




    private List<UML2_ConnectorEnd> uml2_connectorends;


    public UML2_ConnectableElement(
    ) {
        super(
        );
        this.uml2_connectorends = new ArrayList<>();
    }

    public UML2_ConnectableElement(
        ArrayList<UML2_ConnectorEnd> uml2_connectorends    ) {
        this.uml2_connectorends = uml2_connectorends;
    }


    public UML2_StructuredClassifier getUml2_structuredclassifier() {
        return uml2_structuredclassifier;
    }

    public void setUml2_structuredclassifier(UML2_StructuredClassifier uml2_structuredclassifier) {
        this.uml2_structuredclassifier = uml2_structuredclassifier;
    }
    public UML2_ConnectorEnd getUml2_connectorend() {
        return uml2_connectorend;
    }

    public void setUml2_connectorend(UML2_ConnectorEnd uml2_connectorend) {
        this.uml2_connectorend = uml2_connectorend;
    }
    public List<UML2_ConnectorEnd> getUml2_connectorends() {
        return uml2_connectorends;
    }

    public void addUml2_connectorend(Uml2_connectorend uml2_connectorend) {
        this.uml2_connectorends.add(uml2_connectorend);
    }

}