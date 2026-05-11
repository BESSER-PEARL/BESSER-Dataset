





import java.util.List;
import java.util.ArrayList;

public class avm_Component  {

    private String SchemaVersion;
    private String Classifications;
    private String ID;
    private String Version;
    private String Supercedes;
    private String Name;



    public avm_Component(
        String SchemaVersion,        String Classifications,        String ID,        String Version,        String Supercedes,        String Name    ) {
        this.SchemaVersion = SchemaVersion;
        this.Classifications = Classifications;
        this.ID = ID;
        this.Version = Version;
        this.Supercedes = Supercedes;
        this.Name = Name;
    }


    public String getSchemaversion() {
        return SchemaVersion;
    }

    public void setSchemaversion(String SchemaVersion) {
        this.SchemaVersion = SchemaVersion;
    }
    public String getClassifications() {
        return Classifications;
    }

    public void setClassifications(String Classifications) {
        this.Classifications = Classifications;
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


}