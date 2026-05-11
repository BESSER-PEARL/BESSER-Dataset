





import java.util.List;
import java.util.ArrayList;

public class component_SystemDiagram extends IPropertyMap, ModelElement {

    private boolean ConnectorProcessing;
    private String systemId;
    private String updateDate;
    private String creationDate;
    private String kind;





    private component_SystemDiagram component_systemdiagram;


    public component_SystemDiagram(
        boolean ConnectorProcessing,        String systemId,        String updateDate,        String creationDate,        String kind    ) {
        super(
        );
        this.ConnectorProcessing = ConnectorProcessing;
        this.systemId = systemId;
        this.updateDate = updateDate;
        this.creationDate = creationDate;
        this.kind = kind;
    }


    public boolean getConnectorprocessing() {
        return ConnectorProcessing;
    }

    public void setConnectorprocessing(boolean ConnectorProcessing) {
        this.ConnectorProcessing = ConnectorProcessing;
    }
    public String getSystemid() {
        return systemId;
    }

    public void setSystemid(String systemId) {
        this.systemId = systemId;
    }
    public String getUpdatedate() {
        return updateDate;
    }

    public void setUpdatedate(String updateDate) {
        this.updateDate = updateDate;
    }
    public String getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(String creationDate) {
        this.creationDate = creationDate;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public component_SystemDiagram getComponent_systemdiagram() {
        return component_systemdiagram;
    }

    public void setComponent_systemdiagram(component_SystemDiagram component_systemdiagram) {
        this.component_systemdiagram = component_systemdiagram;
    }

}