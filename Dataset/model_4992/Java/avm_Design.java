





import java.util.List;
import java.util.ArrayList;

public class avm_Design  {

    private String Name;
    private String DesignID;
    private String DesignSpaceSrcID;
    private String SchemaVersion;





    private List<avm_DesignDomainFeature> avm_designdomainfeatures;




    private List<avm_Resource> avm_resources;


    public avm_Design(
        String Name,        String DesignID,        String DesignSpaceSrcID,        String SchemaVersion    ) {
        this.Name = Name;
        this.DesignID = DesignID;
        this.DesignSpaceSrcID = DesignSpaceSrcID;
        this.SchemaVersion = SchemaVersion;
        this.avm_designdomainfeatures = new ArrayList<>();
        this.avm_resources = new ArrayList<>();
    }

    public avm_Design(
        String Name,        String DesignID,        String DesignSpaceSrcID,        String SchemaVersion        ArrayList<avm_DesignDomainFeature> avm_designdomainfeatures,        ArrayList<avm_Resource> avm_resources    ) {
        this.Name = Name;
        this.DesignID = DesignID;
        this.DesignSpaceSrcID = DesignSpaceSrcID;
        this.SchemaVersion = SchemaVersion;
        this.avm_designdomainfeatures = avm_designdomainfeatures;
        this.avm_resources = avm_resources;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDesignid() {
        return DesignID;
    }

    public void setDesignid(String DesignID) {
        this.DesignID = DesignID;
    }
    public String getDesignspacesrcid() {
        return DesignSpaceSrcID;
    }

    public void setDesignspacesrcid(String DesignSpaceSrcID) {
        this.DesignSpaceSrcID = DesignSpaceSrcID;
    }
    public String getSchemaversion() {
        return SchemaVersion;
    }

    public void setSchemaversion(String SchemaVersion) {
        this.SchemaVersion = SchemaVersion;
    }

    public List<avm_DesignDomainFeature> getAvm_designdomainfeatures() {
        return avm_designdomainfeatures;
    }

    public void addAvm_designdomainfeature(Avm_designdomainfeature avm_designdomainfeature) {
        this.avm_designdomainfeatures.add(avm_designdomainfeature);
    }
    public List<avm_Resource> getAvm_resources() {
        return avm_resources;
    }

    public void addAvm_resource(Avm_resource avm_resource) {
        this.avm_resources.add(avm_resource);
    }

}