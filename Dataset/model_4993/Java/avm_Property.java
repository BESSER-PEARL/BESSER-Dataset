





import java.util.List;
import java.util.ArrayList;

public class avm_Property  {

    private String ID;
    private String Notes;
    private String Name;
    private String Definition;
    private String XPosition;
    private String YPosition;
    private String OnDataSheet;





    private avm_Container avm_container;




    private avm_Connector avm_connector;


    public avm_Property(
        String ID,        String Notes,        String Name,        String Definition,        String XPosition,        String YPosition,        String OnDataSheet    ) {
        this.ID = ID;
        this.Notes = Notes;
        this.Name = Name;
        this.Definition = Definition;
        this.XPosition = XPosition;
        this.YPosition = YPosition;
        this.OnDataSheet = OnDataSheet;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
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
    public String getDefinition() {
        return Definition;
    }

    public void setDefinition(String Definition) {
        this.Definition = Definition;
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
    public String getOndatasheet() {
        return OnDataSheet;
    }

    public void setOndatasheet(String OnDataSheet) {
        this.OnDataSheet = OnDataSheet;
    }

    public avm_Container getAvm_container() {
        return avm_container;
    }

    public void setAvm_container(avm_Container avm_container) {
        this.avm_container = avm_container;
    }
    public avm_Connector getAvm_connector() {
        return avm_connector;
    }

    public void setAvm_connector(avm_Connector avm_connector) {
        this.avm_connector = avm_connector;
    }

}