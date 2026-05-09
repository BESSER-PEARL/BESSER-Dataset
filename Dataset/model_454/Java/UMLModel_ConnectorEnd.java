





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ConnectorEnd extends MultiplicityElement {

    private String role;
    private String definingEnd;
    private String partWithPort;





    private UMLModel_Connector umlmodel_connector;


    public UMLModel_ConnectorEnd(
        String role,        String definingEnd,        String partWithPort    ) {
        super(
        );
        this.role = role;
        this.definingEnd = definingEnd;
        this.partWithPort = partWithPort;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getDefiningend() {
        return definingEnd;
    }

    public void setDefiningend(String definingEnd) {
        this.definingEnd = definingEnd;
    }
    public String getPartwithport() {
        return partWithPort;
    }

    public void setPartwithport(String partWithPort) {
        this.partWithPort = partWithPort;
    }

    public UMLModel_Connector getUmlmodel_connector() {
        return umlmodel_connector;
    }

    public void setUmlmodel_connector(UMLModel_Connector umlmodel_connector) {
        this.umlmodel_connector = umlmodel_connector;
    }

}