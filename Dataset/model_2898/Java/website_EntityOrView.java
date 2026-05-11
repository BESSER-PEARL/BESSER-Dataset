





import java.util.List;
import java.util.ArrayList;

public class website_EntityOrView extends Classifier {

    private String autoKeyPersistentType;
    private String singletonName;
    private String autoKeyName;
    private String pluralisedName;
    private String autoKeyGenerationStrategy;
    private boolean implementsUserInterface;
    private boolean serializationExcludeAll;
    private String tableName;





    private website_WebGenModel website_webgenmodel;




    private List<website_Service> website_services;




    private website_Service website_service;


    public website_EntityOrView(
        String autoKeyPersistentType,        String singletonName,        String autoKeyName,        String pluralisedName,        String autoKeyGenerationStrategy,        boolean implementsUserInterface,        boolean serializationExcludeAll,        String tableName    ) {
        super(
        );
        this.autoKeyPersistentType = autoKeyPersistentType;
        this.singletonName = singletonName;
        this.autoKeyName = autoKeyName;
        this.pluralisedName = pluralisedName;
        this.autoKeyGenerationStrategy = autoKeyGenerationStrategy;
        this.implementsUserInterface = implementsUserInterface;
        this.serializationExcludeAll = serializationExcludeAll;
        this.tableName = tableName;
        this.website_services = new ArrayList<>();
    }

    public website_EntityOrView(
        String autoKeyPersistentType,        String singletonName,        String autoKeyName,        String pluralisedName,        String autoKeyGenerationStrategy,        boolean implementsUserInterface,        boolean serializationExcludeAll,        String tableName        ArrayList<website_Service> website_services    ) {
        this.autoKeyPersistentType = autoKeyPersistentType;
        this.singletonName = singletonName;
        this.autoKeyName = autoKeyName;
        this.pluralisedName = pluralisedName;
        this.autoKeyGenerationStrategy = autoKeyGenerationStrategy;
        this.implementsUserInterface = implementsUserInterface;
        this.serializationExcludeAll = serializationExcludeAll;
        this.tableName = tableName;
        this.website_services = website_services;
    }

    public String getAutokeypersistenttype() {
        return autoKeyPersistentType;
    }

    public void setAutokeypersistenttype(String autoKeyPersistentType) {
        this.autoKeyPersistentType = autoKeyPersistentType;
    }
    public String getSingletonname() {
        return singletonName;
    }

    public void setSingletonname(String singletonName) {
        this.singletonName = singletonName;
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
    public boolean getImplementsuserinterface() {
        return implementsUserInterface;
    }

    public void setImplementsuserinterface(boolean implementsUserInterface) {
        this.implementsUserInterface = implementsUserInterface;
    }
    public boolean getSerializationexcludeall() {
        return serializationExcludeAll;
    }

    public void setSerializationexcludeall(boolean serializationExcludeAll) {
        this.serializationExcludeAll = serializationExcludeAll;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }

    public website_WebGenModel getWebsite_webgenmodel() {
        return website_webgenmodel;
    }

    public void setWebsite_webgenmodel(website_WebGenModel website_webgenmodel) {
        this.website_webgenmodel = website_webgenmodel;
    }
    public List<website_Service> getWebsite_services() {
        return website_services;
    }

    public void addWebsite_service(Website_service website_service) {
        this.website_services.add(website_service);
    }
    public website_Service getWebsite_service() {
        return website_service;
    }

    public void setWebsite_service(website_Service website_service) {
        this.website_service = website_service;
    }

}