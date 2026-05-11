





import java.util.List;
import java.util.ArrayList;

public class persistence_EntityAttribute extends Attribute, EntityFeature {

    private String ormType;
    private String persistentType;
    private boolean containerUnique;
    private boolean primaryKey;
    private String interfaceType;



    public persistence_EntityAttribute(
        String ormType,        String persistentType,        boolean containerUnique,        boolean primaryKey,        String interfaceType    ) {
        super(
        );
        this.ormType = ormType;
        this.persistentType = persistentType;
        this.containerUnique = containerUnique;
        this.primaryKey = primaryKey;
        this.interfaceType = interfaceType;
    }


    public String getOrmtype() {
        return ormType;
    }

    public void setOrmtype(String ormType) {
        this.ormType = ormType;
    }
    public String getPersistenttype() {
        return persistentType;
    }

    public void setPersistenttype(String persistentType) {
        this.persistentType = persistentType;
    }
    public boolean getContainerunique() {
        return containerUnique;
    }

    public void setContainerunique(boolean containerUnique) {
        this.containerUnique = containerUnique;
    }
    public boolean getPrimarykey() {
        return primaryKey;
    }

    public void setPrimarykey(boolean primaryKey) {
        this.primaryKey = primaryKey;
    }
    public String getInterfacetype() {
        return interfaceType;
    }

    public void setInterfacetype(String interfaceType) {
        this.interfaceType = interfaceType;
    }


}