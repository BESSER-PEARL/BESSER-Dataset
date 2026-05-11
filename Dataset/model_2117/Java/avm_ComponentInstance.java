





import java.util.List;
import java.util.ArrayList;

public class avm_ComponentInstance  {

    private String ComponentID;
    private String Name;
    private String DesignSpaceSrcComponentID;
    private String XPosition;
    private String YPosition;
    private String ID;





    private List<avm_ComponentPortInstance> avm_componentportinstances;




    private List<avm_ComponentConnectorInstance> avm_componentconnectorinstances;


    public avm_ComponentInstance(
        String ComponentID,        String Name,        String DesignSpaceSrcComponentID,        String XPosition,        String YPosition,        String ID    ) {
        this.ComponentID = ComponentID;
        this.Name = Name;
        this.DesignSpaceSrcComponentID = DesignSpaceSrcComponentID;
        this.XPosition = XPosition;
        this.YPosition = YPosition;
        this.ID = ID;
        this.avm_componentportinstances = new ArrayList<>();
        this.avm_componentconnectorinstances = new ArrayList<>();
    }

    public avm_ComponentInstance(
        String ComponentID,        String Name,        String DesignSpaceSrcComponentID,        String XPosition,        String YPosition,        String ID        ArrayList<avm_ComponentPortInstance> avm_componentportinstances,        ArrayList<avm_ComponentConnectorInstance> avm_componentconnectorinstances    ) {
        this.ComponentID = ComponentID;
        this.Name = Name;
        this.DesignSpaceSrcComponentID = DesignSpaceSrcComponentID;
        this.XPosition = XPosition;
        this.YPosition = YPosition;
        this.ID = ID;
        this.avm_componentportinstances = avm_componentportinstances;
        this.avm_componentconnectorinstances = avm_componentconnectorinstances;
    }

    public String getComponentid() {
        return ComponentID;
    }

    public void setComponentid(String ComponentID) {
        this.ComponentID = ComponentID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDesignspacesrccomponentid() {
        return DesignSpaceSrcComponentID;
    }

    public void setDesignspacesrccomponentid(String DesignSpaceSrcComponentID) {
        this.DesignSpaceSrcComponentID = DesignSpaceSrcComponentID;
    }
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<avm_ComponentPortInstance> getAvm_componentportinstances() {
        return avm_componentportinstances;
    }

    public void addAvm_componentportinstance(Avm_componentportinstance avm_componentportinstance) {
        this.avm_componentportinstances.add(avm_componentportinstance);
    }
    public List<avm_ComponentConnectorInstance> getAvm_componentconnectorinstances() {
        return avm_componentconnectorinstances;
    }

    public void addAvm_componentconnectorinstance(Avm_componentconnectorinstance avm_componentconnectorinstance) {
        this.avm_componentconnectorinstances.add(avm_componentconnectorinstance);
    }

}