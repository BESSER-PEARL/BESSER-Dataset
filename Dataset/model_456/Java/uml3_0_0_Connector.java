





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Connector extends Feature {

    private String kind;





    private uml3_0_0_Association uml3_0_0_association;




    private List<uml3_0_0_Connector> uml3_0_0_connectors;




    private uml3_0_0_Message uml3_0_0_message;




    private List<uml3_0_0_ConnectorEnd> uml3_0_0_connectorends;




    private uml3_0_0_InformationFlow uml3_0_0_informationflow;




    private List<uml3_0_0_Behavior> uml3_0_0_behaviors;




    private uml3_0_0_StructuredClassifier uml3_0_0_structuredclassifier;


    public uml3_0_0_Connector(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.uml3_0_0_connectors = new ArrayList<>();
        this.uml3_0_0_connectorends = new ArrayList<>();
        this.uml3_0_0_behaviors = new ArrayList<>();
    }

    public uml3_0_0_Connector(
        String kind        ArrayList<uml3_0_0_Connector> uml3_0_0_connectors,        ArrayList<uml3_0_0_ConnectorEnd> uml3_0_0_connectorends,        ArrayList<uml3_0_0_Behavior> uml3_0_0_behaviors    ) {
        this.kind = kind;
        this.uml3_0_0_connectors = uml3_0_0_connectors;
        this.uml3_0_0_connectorends = uml3_0_0_connectorends;
        this.uml3_0_0_behaviors = uml3_0_0_behaviors;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public uml3_0_0_Association getUml3_0_0_association() {
        return uml3_0_0_association;
    }

    public void setUml3_0_0_association(uml3_0_0_Association uml3_0_0_association) {
        this.uml3_0_0_association = uml3_0_0_association;
    }
    public List<uml3_0_0_Connector> getUml3_0_0_connectors() {
        return uml3_0_0_connectors;
    }

    public void addUml3_0_0_connector(Uml3_0_0_connector uml3_0_0_connector) {
        this.uml3_0_0_connectors.add(uml3_0_0_connector);
    }
    public uml3_0_0_Message getUml3_0_0_message() {
        return uml3_0_0_message;
    }

    public void setUml3_0_0_message(uml3_0_0_Message uml3_0_0_message) {
        this.uml3_0_0_message = uml3_0_0_message;
    }
    public List<uml3_0_0_ConnectorEnd> getUml3_0_0_connectorends() {
        return uml3_0_0_connectorends;
    }

    public void addUml3_0_0_connectorend(Uml3_0_0_connectorend uml3_0_0_connectorend) {
        this.uml3_0_0_connectorends.add(uml3_0_0_connectorend);
    }
    public uml3_0_0_InformationFlow getUml3_0_0_informationflow() {
        return uml3_0_0_informationflow;
    }

    public void setUml3_0_0_informationflow(uml3_0_0_InformationFlow uml3_0_0_informationflow) {
        this.uml3_0_0_informationflow = uml3_0_0_informationflow;
    }
    public List<uml3_0_0_Behavior> getUml3_0_0_behaviors() {
        return uml3_0_0_behaviors;
    }

    public void addUml3_0_0_behavior(Uml3_0_0_behavior uml3_0_0_behavior) {
        this.uml3_0_0_behaviors.add(uml3_0_0_behavior);
    }
    public uml3_0_0_StructuredClassifier getUml3_0_0_structuredclassifier() {
        return uml3_0_0_structuredclassifier;
    }

    public void setUml3_0_0_structuredclassifier(uml3_0_0_StructuredClassifier uml3_0_0_structuredclassifier) {
        this.uml3_0_0_structuredclassifier = uml3_0_0_structuredclassifier;
    }

}