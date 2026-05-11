





import java.util.List;
import java.util.ArrayList;

public class website_EntityAttribute extends EntityFeature, Attribute {

    private String interfaceType;
    private boolean containerUnique;
    private String persistentType;
    private String ormType;
    private boolean primaryKey;



    public website_EntityAttribute(
        String interfaceType,        boolean containerUnique,        String persistentType,        String ormType,        boolean primaryKey    ) {
        super(
        );
        this.interfaceType = interfaceType;
        this.containerUnique = containerUnique;
        this.persistentType = persistentType;
        this.ormType = ormType;
        this.primaryKey = primaryKey;
    }


    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
    }
    public boolean getContainerunique() {
        return containerUnique;
    }

    public void setContainerunique(boolean containerUnique) {
        this.containerUnique = containerUnique;
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
    public boolean getPrimarykey() {
        return primaryKey;
    }

    public void setPrimarykey(boolean primaryKey) {
        this.primaryKey = primaryKey;
    }


}