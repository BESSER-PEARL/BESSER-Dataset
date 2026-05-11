





import java.util.List;
import java.util.ArrayList;

public class persistence_Entity extends Classifier {

    private String singletonName;
    private String tableName;
    private String autoKeyPersistentType;
    private String autoKeyGenerationStrategy;
    private String autoKeyName;
    private String pluralisedName;
    private boolean allowFormTypeCustomisation;
    private boolean implementsUserInterface;





    private persistence_Feature persistence_feature;




    private List<persistence_Feature> persistence_features;




    private List<persistence_Feature> persistence_features;




    private List<persistence_Feature> persistence_features;




    private persistence_Persistence persistence_persistence;




    private List<persistence_Feature> persistence_features;




    private List<persistence_Feature> persistence_features;


    public persistence_Entity(
        String singletonName,        String tableName,        String autoKeyPersistentType,        String autoKeyGenerationStrategy,        String autoKeyName,        String pluralisedName,        boolean allowFormTypeCustomisation,        boolean implementsUserInterface    ) {
        super(
        );
        this.singletonName = singletonName;
        this.tableName = tableName;
        this.autoKeyPersistentType = autoKeyPersistentType;
        this.autoKeyGenerationStrategy = autoKeyGenerationStrategy;
        this.autoKeyName = autoKeyName;
        this.pluralisedName = pluralisedName;
        this.allowFormTypeCustomisation = allowFormTypeCustomisation;
        this.implementsUserInterface = implementsUserInterface;
        this.persistence_features = new ArrayList<>();
        this.persistence_features = new ArrayList<>();
        this.persistence_features = new ArrayList<>();
        this.persistence_features = new ArrayList<>();
        this.persistence_features = new ArrayList<>();
    }

    public persistence_Entity(
        String singletonName,        String tableName,        String autoKeyPersistentType,        String autoKeyGenerationStrategy,        String autoKeyName,        String pluralisedName,        boolean allowFormTypeCustomisation,        boolean implementsUserInterface        ArrayList<persistence_Feature> persistence_features,        ArrayList<persistence_Feature> persistence_features,        ArrayList<persistence_Feature> persistence_features,        ArrayList<persistence_Feature> persistence_features,        ArrayList<persistence_Feature> persistence_features    ) {
        this.singletonName = singletonName;
        this.tableName = tableName;
        this.autoKeyPersistentType = autoKeyPersistentType;
        this.autoKeyGenerationStrategy = autoKeyGenerationStrategy;
        this.autoKeyName = autoKeyName;
        this.pluralisedName = pluralisedName;
        this.allowFormTypeCustomisation = allowFormTypeCustomisation;
        this.implementsUserInterface = implementsUserInterface;
        this.persistence_features = persistence_features;
        this.persistence_features = persistence_features;
        this.persistence_features = persistence_features;
        this.persistence_features = persistence_features;
        this.persistence_features = persistence_features;
    }

    public String getSingletonname() {
        return singletonName;
    }

    public void setSingletonname(String singletonName) {
        this.singletonName = singletonName;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getAutokeypersistenttype() {
        return autoKeyPersistentType;
    }

    public void setAutokeypersistenttype(String autoKeyPersistentType) {
        this.autoKeyPersistentType = autoKeyPersistentType;
    }
    public String getAutokeygenerationstrategy() {
        return autoKeyGenerationStrategy;
    }

    public void setAutokeygenerationstrategy(String autoKeyGenerationStrategy) {
        this.autoKeyGenerationStrategy = autoKeyGenerationStrategy;
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
    public boolean getAllowformtypecustomisation() {
        return allowFormTypeCustomisation;
    }

    public void setAllowformtypecustomisation(boolean allowFormTypeCustomisation) {
        this.allowFormTypeCustomisation = allowFormTypeCustomisation;
    }
    public boolean getImplementsuserinterface() {
        return implementsUserInterface;
    }

    public void setImplementsuserinterface(boolean implementsUserInterface) {
        this.implementsUserInterface = implementsUserInterface;
    }

    public persistence_Feature getPersistence_feature() {
        return persistence_feature;
    }

    public void setPersistence_feature(persistence_Feature persistence_feature) {
        this.persistence_feature = persistence_feature;
    }
    public List<persistence_Feature> getPersistence_features() {
        return persistence_features;
    }

    public void addPersistence_feature(Persistence_feature persistence_feature) {
        this.persistence_features.add(persistence_feature);
    }
    public List<persistence_Feature> getPersistence_features() {
        return persistence_features;
    }

    public void addPersistence_feature(Persistence_feature persistence_feature) {
        this.persistence_features.add(persistence_feature);
    }
    public List<persistence_Feature> getPersistence_features() {
        return persistence_features;
    }

    public void addPersistence_feature(Persistence_feature persistence_feature) {
        this.persistence_features.add(persistence_feature);
    }
    public persistence_Persistence getPersistence_persistence() {
        return persistence_persistence;
    }

    public void setPersistence_persistence(persistence_Persistence persistence_persistence) {
        this.persistence_persistence = persistence_persistence;
    }
    public List<persistence_Feature> getPersistence_features() {
        return persistence_features;
    }

    public void addPersistence_feature(Persistence_feature persistence_feature) {
        this.persistence_features.add(persistence_feature);
    }
    public List<persistence_Feature> getPersistence_features() {
        return persistence_features;
    }

    public void addPersistence_feature(Persistence_feature persistence_feature) {
        this.persistence_features.add(persistence_feature);
    }

}