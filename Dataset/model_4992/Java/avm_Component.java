





import java.util.List;
import java.util.ArrayList;

public class avm_Component  {

    private String ID;
    private String Version;
    private String Classifications;
    private String Supercedes;
    private String Name;
    private String SchemaVersion;



    public avm_Component(
        String ID,        String Version,        String Classifications,        String Supercedes,        String Name,        String SchemaVersion    ) {
        this.ID = ID;
        this.Version = Version;
        this.Classifications = Classifications;
        this.Supercedes = Supercedes;
        this.Name = Name;
        this.SchemaVersion = SchemaVersion;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getVersion() {
        return Version;
    }

    public void setVersion(String Version) {
        this.Version = Version;
    }
    public String getClassifications() {
        return Classifications;
    }

    public void setClassifications(String Classifications) {
        this.Classifications = Classifications;
    }
    public String getSupercedes() {
        return Supercedes;
    }

    public void setSupercedes(String Supercedes) {
        this.Supercedes = Supercedes;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getSchemaversion() {
        return SchemaVersion;
    }

    public void setSchemaversion(String SchemaVersion) {
        this.SchemaVersion = SchemaVersion;
    }


}