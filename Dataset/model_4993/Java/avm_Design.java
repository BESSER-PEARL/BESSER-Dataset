





import java.util.List;
import java.util.ArrayList;

public class avm_Design  {

    private String SchemaVersion;
    private String Name;
    private String DesignSpaceSrcID;
    private String DesignID;



    public avm_Design(
        String SchemaVersion,        String Name,        String DesignSpaceSrcID,        String DesignID    ) {
        this.SchemaVersion = SchemaVersion;
        this.Name = Name;
        this.DesignSpaceSrcID = DesignSpaceSrcID;
        this.DesignID = DesignID;
    }


    public String getSchemaversion() {
        return SchemaVersion;
    }

    public void setSchemaversion(String SchemaVersion) {
        this.SchemaVersion = SchemaVersion;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDesignspacesrcid() {
        return DesignSpaceSrcID;
    }

    public void setDesignspacesrcid(String DesignSpaceSrcID) {
        this.DesignSpaceSrcID = DesignSpaceSrcID;
    }
    public String getDesignid() {
        return DesignID;
    }

    public void setDesignid(String DesignID) {
        this.DesignID = DesignID;
    }


}