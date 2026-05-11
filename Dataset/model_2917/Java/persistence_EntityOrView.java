





import java.util.List;
import java.util.ArrayList;

public class persistence_EntityOrView extends Classifier {

    private boolean implementsUserInterface;
    private String autoKeyPersistentType;
    private String autoKeyName;
    private String pluralisedName;
    private String autoKeyGenerationStrategy;
    private String tableName;
    private String singletonName;





    private persistence_Persistence persistence_persistence;


    public persistence_EntityOrView(
        boolean implementsUserInterface,        String autoKeyPersistentType,        String autoKeyName,        String pluralisedName,        String autoKeyGenerationStrategy,        String tableName,        String singletonName    ) {
        super(
        );
        this.implementsUserInterface = implementsUserInterface;
        this.autoKeyPersistentType = autoKeyPersistentType;
        this.autoKeyName = autoKeyName;
        this.pluralisedName = pluralisedName;
        this.autoKeyGenerationStrategy = autoKeyGenerationStrategy;
        this.tableName = tableName;
        this.singletonName = singletonName;
    }


    public boolean getImplementsuserinterface() {
        return implementsUserInterface;
    }

    public void setImplementsuserinterface(boolean implementsUserInterface) {
        this.implementsUserInterface = implementsUserInterface;
    }
    public String getAutokeypersistenttype() {
        return autoKeyPersistentType;
    }

    public void setAutokeypersistenttype(String autoKeyPersistentType) {
        this.autoKeyPersistentType = autoKeyPersistentType;
    }
    public String getAutokeyname() {
        return autoKeyName;
    }

    public void setAutokeyname(String autoKeyName) {
        this.autoKeyName = autoKeyName;
    }
    public String getPluralisedname() {
        return pluralisedName;
    }

    public void setPluralisedname(String pluralisedName) {
        this.pluralisedName = pluralisedName;
    }
    public String getAutokeygenerationstrategy() {
        return autoKeyGenerationStrategy;
    }

    public void setAutokeygenerationstrategy(String autoKeyGenerationStrategy) {
        this.autoKeyGenerationStrategy = autoKeyGenerationStrategy;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getSingletonname() {
        return singletonName;
    }

    public void setSingletonname(String singletonName) {
        this.singletonName = singletonName;
    }

    public persistence_Persistence getPersistence_persistence() {
        return persistence_persistence;
    }

    public void setPersistence_persistence(persistence_Persistence persistence_persistence) {
        this.persistence_persistence = persistence_persistence;
    }

}