





import java.util.List;
import java.util.ArrayList;

public class avm_Connector extends ConnectorCompositionTarget {

    private String Definition;
    private String YPosition;
    private String Notes;
    private String XPosition;
    private String Name;





    private List<avm_Property> avm_propertys;




    private avm_Connector avm_connector;




    private avm_Component avm_component;


    public avm_Connector(
        String Definition,        String YPosition,        String Notes,        String XPosition,        String Name    ) {
        super(
        );
        this.Definition = Definition;
        this.YPosition = YPosition;
        this.Notes = Notes;
        this.XPosition = XPosition;
        this.Name = Name;
        this.avm_propertys = new ArrayList<>();
    }

    public avm_Connector(
        String Definition,        String YPosition,        String Notes,        String XPosition,        String Name        ArrayList<avm_Property> avm_propertys    ) {
        this.Definition = Definition;
        this.YPosition = YPosition;
        this.Notes = Notes;
        this.XPosition = XPosition;
        this.Name = Name;
        this.avm_propertys = avm_propertys;
    }

    public String getDefinition() {
        return Definition;
    }

    public void setDefinition(String Definition) {
        this.Definition = Definition;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<avm_Property> getAvm_propertys() {
        return avm_propertys;
    }

    public void addAvm_property(Avm_property avm_property) {
        this.avm_propertys.add(avm_property);
    }
    public avm_Connector getAvm_connector() {
        return avm_connector;
    }

    public void setAvm_connector(avm_Connector avm_connector) {
        this.avm_connector = avm_connector;
    }
    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}