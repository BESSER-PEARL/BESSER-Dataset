





import java.util.List;
import java.util.ArrayList;

public class avm_Property  {

    private String Definition;
    private String OnDataSheet;
    private String XPosition;
    private String Notes;
    private String Name;
    private String YPosition;
    private String ID;





    private avm_Component avm_component;


    public avm_Property(
        String Definition,        String OnDataSheet,        String XPosition,        String Notes,        String Name,        String YPosition,        String ID    ) {
        this.Definition = Definition;
        this.OnDataSheet = OnDataSheet;
        this.XPosition = XPosition;
        this.Notes = Notes;
        this.Name = Name;
        this.YPosition = YPosition;
        this.ID = ID;
    }


    public String getDefinition() {
        return Definition;
    }

    public void setDefinition(String Definition) {
        this.Definition = Definition;
    }
    public String getOndatasheet() {
        return OnDataSheet;
    }

    public void setOndatasheet(String OnDataSheet) {
        this.OnDataSheet = OnDataSheet;
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
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}