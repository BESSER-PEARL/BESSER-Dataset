





import java.util.List;
import java.util.ArrayList;

public class avm_Port extends PortMapTarget {

    private String YPosition;
    private String Name;
    private String XPosition;
    private String Notes;
    private String Definition;





    private avm_Connector avm_connector;




    private avm_Component avm_component;


    public avm_Port(
        String YPosition,        String Name,        String XPosition,        String Notes,        String Definition    ) {
        super(
        );
        this.YPosition = YPosition;
        this.Name = Name;
        this.XPosition = XPosition;
        this.Notes = Notes;
        this.Definition = Definition;
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
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }
    public String getDefinition() {
        return Definition;
    }

    public void setDefinition(String Definition) {
        this.Definition = Definition;
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