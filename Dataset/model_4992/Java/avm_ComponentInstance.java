





import java.util.List;
import java.util.ArrayList;

public class avm_ComponentInstance  {

    private String XPosition;
    private String Name;
    private String ID;
    private String ComponentID;
    private String YPosition;
    private String DesignSpaceSrcComponentID;





    private List<avm_ComponentConnectorInstance> avm_componentconnectorinstances;




    private List<avm_ComponentPortInstance> avm_componentportinstances;


    public avm_ComponentInstance(
        String XPosition,        String Name,        String ID,        String ComponentID,        String YPosition,        String DesignSpaceSrcComponentID    ) {
        this.XPosition = XPosition;
        this.Name = Name;
        this.ID = ID;
        this.ComponentID = ComponentID;
        this.YPosition = YPosition;
        this.DesignSpaceSrcComponentID = DesignSpaceSrcComponentID;
        this.avm_componentconnectorinstances = new ArrayList<>();
        this.avm_componentportinstances = new ArrayList<>();
    }

    public avm_ComponentInstance(
        String XPosition,        String Name,        String ID,        String ComponentID,        String YPosition,        String DesignSpaceSrcComponentID        ArrayList<avm_ComponentConnectorInstance> avm_componentconnectorinstances,        ArrayList<avm_ComponentPortInstance> avm_componentportinstances    ) {
        this.XPosition = XPosition;
        this.Name = Name;
        this.ID = ID;
        this.ComponentID = ComponentID;
        this.YPosition = YPosition;
        this.DesignSpaceSrcComponentID = DesignSpaceSrcComponentID;
        this.avm_componentconnectorinstances = avm_componentconnectorinstances;
        this.avm_componentportinstances = avm_componentportinstances;
    }

    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getComponentid() {
        return ComponentID;
    }

    public void setComponentid(String ComponentID) {
        this.ComponentID = ComponentID;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getDesignspacesrccomponentid() {
        return DesignSpaceSrcComponentID;
    }

    public void setDesignspacesrccomponentid(String DesignSpaceSrcComponentID) {
        this.DesignSpaceSrcComponentID = DesignSpaceSrcComponentID;
    }

    public List<avm_ComponentConnectorInstance> getAvm_componentconnectorinstances() {
        return avm_componentconnectorinstances;
    }

    public void addAvm_componentconnectorinstance(Avm_componentconnectorinstance avm_componentconnectorinstance) {
        this.avm_componentconnectorinstances.add(avm_componentconnectorinstance);
    }
    public List<avm_ComponentPortInstance> getAvm_componentportinstances() {
        return avm_componentportinstances;
    }

    public void addAvm_componentportinstance(Avm_componentportinstance avm_componentportinstance) {
        this.avm_componentportinstances.add(avm_componentportinstance);
    }

}