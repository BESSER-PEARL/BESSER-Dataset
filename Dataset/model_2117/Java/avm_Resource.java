





import java.util.List;
import java.util.ArrayList;

public class avm_Resource  {

    private String Path;
    private String ID;
    private String Name;
    private String XPosition;
    private String YPosition;
    private String Hash;
    private String Notes;





    private avm_Component avm_component;




    private avm_DomainModel_ avm_domainmodel_;


    public avm_Resource(
        String Path,        String ID,        String Name,        String XPosition,        String YPosition,        String Hash,        String Notes    ) {
        this.Path = Path;
        this.ID = ID;
        this.Name = Name;
        this.XPosition = XPosition;
        this.YPosition = YPosition;
        this.Hash = Hash;
        this.Notes = Notes;
    }


    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
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
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getHash() {
        return Hash;
    }

    public void setHash(String Hash) {
        this.Hash = Hash;
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
    public avm_DomainModel_ getAvm_domainmodel_() {
        return avm_domainmodel_;
    }

    public void setAvm_domainmodel_(avm_DomainModel_ avm_domainmodel_) {
        this.avm_domainmodel_ = avm_domainmodel_;
    }

}