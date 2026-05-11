





import java.util.List;
import java.util.ArrayList;

public class avm_Design  {

    private String SchemaVersion;
    private String DesignSpaceSrcID;
    private String DesignID;
    private String Name;



    public avm_Design(
        String SchemaVersion,        String DesignSpaceSrcID,        String DesignID,        String Name    ) {
        this.SchemaVersion = SchemaVersion;
        this.DesignSpaceSrcID = DesignSpaceSrcID;
        this.DesignID = DesignID;
        this.Name = Name;
    }


    public String getSchemaversion() {
        return SchemaVersion;
    }

    public void setSchemaversion(String SchemaVersion) {
        this.SchemaVersion = SchemaVersion;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}