





import java.util.List;
import java.util.ArrayList;

public class avm_Connector extends ConnectorCompositionTarget {

    private String YPosition;
    private String XPosition;
    private String Definition;
    private String Name;
    private String Notes;





    private avm_Connector avm_connector;


    public avm_Connector(
        String YPosition,        String XPosition,        String Definition,        String Name,        String Notes    ) {
        super(
        );
        this.YPosition = YPosition;
        this.XPosition = XPosition;
        this.Definition = Definition;
        this.Name = Name;
        this.Notes = Notes;
    }


    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getDefinition() {
        return Definition;
    }

    public void setDefinition(String Definition) {
        this.Definition = Definition;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }

    public avm_Connector getAvm_connector() {
        return avm_connector;
    }

    public void setAvm_connector(avm_Connector avm_connector) {
        this.avm_connector = avm_connector;
    }

}