





import java.util.List;
import java.util.ArrayList;

public class avm_Connector extends ConnectorCompositionTarget {

    private String YPosition;
    private String Name;
    private String Definition;
    private String Notes;
    private String XPosition;





    private List<avm_Property> avm_propertys;




    private List<avm_Connector> avm_connectors;




    private avm_Component avm_component;


    public avm_Connector(
        String YPosition,        String Name,        String Definition,        String Notes,        String XPosition    ) {
        super(
        );
        this.YPosition = YPosition;
        this.Name = Name;
        this.Definition = Definition;
        this.Notes = Notes;
        this.XPosition = XPosition;
        this.avm_propertys = new ArrayList<>();
        this.avm_connectors = new ArrayList<>();
    }

    public avm_Connector(
        String YPosition,        String Name,        String Definition,        String Notes,        String XPosition        ArrayList<avm_Property> avm_propertys,        ArrayList<avm_Connector> avm_connectors    ) {
        this.YPosition = YPosition;
        this.Name = Name;
        this.Definition = Definition;
        this.Notes = Notes;
        this.XPosition = XPosition;
        this.avm_propertys = avm_propertys;
        this.avm_connectors = avm_connectors;
    }

    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDefinition() {
        return Definition;
    }

    public void setDefinition(String Definition) {
        this.Definition = Definition;
    }
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }

    public List<avm_Property> getAvm_propertys() {
        return avm_propertys;
    }

    public void addAvm_property(Avm_property avm_property) {
        this.avm_propertys.add(avm_property);
    }
    public List<avm_Connector> getAvm_connectors() {
        return avm_connectors;
    }

    public void addAvm_connector(Avm_connector avm_connector) {
        this.avm_connectors.add(avm_connector);
    }
    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}