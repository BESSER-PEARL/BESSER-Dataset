





import java.util.List;
import java.util.ArrayList;

public class uml_Connector extends Feature {

    private String kind;





    private uml_Message uml_message;




    private uml_StructuredClassifier uml_structuredclassifier;




    private List<uml_Behavior> uml_behaviors;




    private List<uml_Connector> uml_connectors;




    private uml_Association uml_association;




    private uml_InformationFlow uml_informationflow;




    private List<uml_ConnectorEnd> uml_connectorends;


    public uml_Connector(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.uml_behaviors = new ArrayList<>();
        this.uml_connectors = new ArrayList<>();
        this.uml_connectorends = new ArrayList<>();
    }

    public uml_Connector(
        String kind        ArrayList<uml_Behavior> uml_behaviors,        ArrayList<uml_Connector> uml_connectors,        ArrayList<uml_ConnectorEnd> uml_connectorends    ) {
        this.kind = kind;
        this.uml_behaviors = uml_behaviors;
        this.uml_connectors = uml_connectors;
        this.uml_connectorends = uml_connectorends;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public uml_Message getUml_message() {
        return uml_message;
    }

    public void setUml_message(uml_Message uml_message) {
        this.uml_message = uml_message;
    }
    public uml_StructuredClassifier getUml_structuredclassifier() {
        return uml_structuredclassifier;
    }

    public void setUml_structuredclassifier(uml_StructuredClassifier uml_structuredclassifier) {
        this.uml_structuredclassifier = uml_structuredclassifier;
    }
    public List<uml_Behavior> getUml_behaviors() {
        return uml_behaviors;
    }

    public void addUml_behavior(Uml_behavior uml_behavior) {
        this.uml_behaviors.add(uml_behavior);
    }
    public List<uml_Connector> getUml_connectors() {
        return uml_connectors;
    }

    public void addUml_connector(Uml_connector uml_connector) {
        this.uml_connectors.add(uml_connector);
    }
    public uml_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(uml_Association uml_association) {
        this.uml_association = uml_association;
    }
    public uml_InformationFlow getUml_informationflow() {
        return uml_informationflow;
    }

    public void setUml_informationflow(uml_InformationFlow uml_informationflow) {
        this.uml_informationflow = uml_informationflow;
    }
    public List<uml_ConnectorEnd> getUml_connectorends() {
        return uml_connectorends;
    }

    public void addUml_connectorend(Uml_connectorend uml_connectorend) {
        this.uml_connectorends.add(uml_connectorend);
    }

}