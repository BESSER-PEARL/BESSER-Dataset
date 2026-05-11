





import java.util.List;
import java.util.ArrayList;

public class persistence_EntityAttribute extends EntityFeature, Attribute {

    private String interfaceType;
    private boolean unique;
    private boolean containerUnique;
    private boolean hidden;
    private String persistentType;
    private String ormType;





    private List<persistence_Attribute> persistence_attributes;


    public persistence_EntityAttribute(
        String interfaceType,        boolean unique,        boolean containerUnique,        boolean hidden,        String persistentType,        String ormType    ) {
        super(
        );
        this.interfaceType = interfaceType;
        this.unique = unique;
        this.containerUnique = containerUnique;
        this.hidden = hidden;
        this.persistentType = persistentType;
        this.ormType = ormType;
        this.persistence_attributes = new ArrayList<>();
    }

    public persistence_EntityAttribute(
        String interfaceType,        boolean unique,        boolean containerUnique,        boolean hidden,        String persistentType,        String ormType        ArrayList<persistence_Attribute> persistence_attributes    ) {
        this.interfaceType = interfaceType;
        this.unique = unique;
        this.containerUnique = containerUnique;
        this.hidden = hidden;
        this.persistentType = persistentType;
        this.ormType = ormType;
        this.persistence_attributes = persistence_attributes;
    }

    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getContainerunique() {
        return containerUnique;
    }

    public void setContainerunique(boolean containerUnique) {
        this.containerUnique = containerUnique;
    }
    public boolean getHidden() {
        return hidden;
    }

    public void setHidden(boolean hidden) {
        this.hidden = hidden;
    }
    public String getPersistenttype() {
        return persistentType;
    }

    public void setPersistenttype(String persistentType) {
        this.persistentType = persistentType;
    }
    public String getOrmtype() {
        return ormType;
    }

    public void setOrmtype(String ormType) {
        this.ormType = ormType;
    }

    public List<persistence_Attribute> getPersistence_attributes() {
        return persistence_attributes;
    }

    public void addPersistence_attribute(Persistence_attribute persistence_attribute) {
        this.persistence_attributes.add(persistence_attribute);
    }

}