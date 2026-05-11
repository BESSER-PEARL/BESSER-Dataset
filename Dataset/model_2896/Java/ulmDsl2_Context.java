





import java.util.List;
import java.util.ArrayList;

public class ulmDsl2_Context  {

    private String version;
    private String name;





    private List<ulmDsl2_Attribute> ulmdsl2_attributes;




    private List<ulmDsl2_Lookup> ulmdsl2_lookups;




    private ulmDsl2_Model ulmdsl2_model;




    private List<ulmDsl2_Entity> ulmdsl2_entitys;


    public ulmDsl2_Context(
        String version,        String name    ) {
        this.version = version;
        this.name = name;
        this.ulmdsl2_attributes = new ArrayList<>();
        this.ulmdsl2_lookups = new ArrayList<>();
        this.ulmdsl2_entitys = new ArrayList<>();
    }

    public ulmDsl2_Context(
        String version,        String name        ArrayList<ulmDsl2_Attribute> ulmdsl2_attributes,        ArrayList<ulmDsl2_Lookup> ulmdsl2_lookups,        ArrayList<ulmDsl2_Entity> ulmdsl2_entitys    ) {
        this.version = version;
        this.name = name;
        this.ulmdsl2_attributes = ulmdsl2_attributes;
        this.ulmdsl2_lookups = ulmdsl2_lookups;
        this.ulmdsl2_entitys = ulmdsl2_entitys;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ulmDsl2_Attribute> getUlmdsl2_attributes() {
        return ulmdsl2_attributes;
    }

    public void addUlmdsl2_attribute(Ulmdsl2_attribute ulmdsl2_attribute) {
        this.ulmdsl2_attributes.add(ulmdsl2_attribute);
    }
    public List<ulmDsl2_Lookup> getUlmdsl2_lookups() {
        return ulmdsl2_lookups;
    }

    public void addUlmdsl2_lookup(Ulmdsl2_lookup ulmdsl2_lookup) {
        this.ulmdsl2_lookups.add(ulmdsl2_lookup);
    }
    public ulmDsl2_Model getUlmdsl2_model() {
        return ulmdsl2_model;
    }

    public void setUlmdsl2_model(ulmDsl2_Model ulmdsl2_model) {
        this.ulmdsl2_model = ulmdsl2_model;
    }
    public List<ulmDsl2_Entity> getUlmdsl2_entitys() {
        return ulmdsl2_entitys;
    }

    public void addUlmdsl2_entity(Ulmdsl2_entity ulmdsl2_entity) {
        this.ulmdsl2_entitys.add(ulmdsl2_entity);
    }

}