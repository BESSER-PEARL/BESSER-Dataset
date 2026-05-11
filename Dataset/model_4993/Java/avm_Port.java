





import java.util.List;
import java.util.ArrayList;

public class avm_Port extends PortMapTarget {

    private String XPosition;
    private String Definition;
    private String Notes;
    private String Name;
    private String YPosition;





    private avm_Connector avm_connector;


    public avm_Port(
        String XPosition,        String Definition,        String Notes,        String Name,        String YPosition    ) {
        super(
        );
        this.XPosition = XPosition;
        this.Definition = Definition;
        this.Notes = Notes;
        this.Name = Name;
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
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }

    public avm_Connector getAvm_connector() {
        return avm_connector;
    }

    public void setAvm_connector(avm_Connector avm_connector) {
        this.avm_connector = avm_connector;
    }

}