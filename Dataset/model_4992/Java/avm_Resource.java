





import java.util.List;
import java.util.ArrayList;

public class avm_Resource  {

    private String Name;
    private String XPosition;
    private String Hash;
    private String ID;
    private String Path;
    private String YPosition;
    private String Notes;





    private avm_Component avm_component;


    public avm_Resource(
        String Name,        String XPosition,        String Hash,        String ID,        String Path,        String YPosition,        String Notes    ) {
        this.Name = Name;
        this.XPosition = XPosition;
        this.Hash = Hash;
        this.ID = ID;
        this.Path = Path;
        this.YPosition = YPosition;
        this.Notes = Notes;
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
    public String getHash() {
        return Hash;
    }

    public void setHash(String Hash) {
        this.Hash = Hash;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
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

    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }

}