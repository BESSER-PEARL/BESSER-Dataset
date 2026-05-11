





import java.util.List;
import java.util.ArrayList;

public class component_SystemDiagram extends ModelElement, IPropertyMap {

    private String creationDate;
    private String updateDate;
    private String kind;
    private String systemId;
    private boolean ConnectorProcessing;





    private component_SystemDiagram component_systemdiagram;


    public component_SystemDiagram(
        String creationDate,        String updateDate,        String kind,        String systemId,        boolean ConnectorProcessing    ) {
        super(
        );
        this.creationDate = creationDate;
        this.updateDate = updateDate;
        this.kind = kind;
        this.systemId = systemId;
        this.ConnectorProcessing = ConnectorProcessing;
    }


    public String getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(String creationDate) {
        this.creationDate = creationDate;
    }
    public String getUpdatedate() {
        return updateDate;
    }

    public void setUpdatedate(String updateDate) {
        this.updateDate = updateDate;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getSystemid() {
        return systemId;
    }

    public void setSystemid(String systemId) {
        this.systemId = systemId;
    }
    public boolean getConnectorprocessing() {
        return ConnectorProcessing;
    }

    public void setConnectorprocessing(boolean ConnectorProcessing) {
        this.ConnectorProcessing = ConnectorProcessing;
    }

    public component_SystemDiagram getComponent_systemdiagram() {
        return component_systemdiagram;
    }

    public void setComponent_systemdiagram(component_SystemDiagram component_systemdiagram) {
        this.component_systemdiagram = component_systemdiagram;
    }

}