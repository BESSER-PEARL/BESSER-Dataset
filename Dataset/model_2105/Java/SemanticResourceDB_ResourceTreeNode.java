





import java.util.List;
import java.util.ArrayList;

public class SemanticResourceDB_ResourceTreeNode  {

    private boolean exists;
    private String name;
    private String queryPart;
    private String sessionProperties;
    private String type;
    private boolean localOnly;
    private String dynamicContentProviderID;
    private String path;
    private String templateID;
    private String remoteURI;
    private String persistentProperties;





    private SemanticResourceDB_ResourceTreeNode semanticresourcedb_resourcetreenode;




    private SemanticResourceDB_ResourceTreeNode semanticresourcedb_resourcetreenode;


    public SemanticResourceDB_ResourceTreeNode(
        boolean exists,        String name,        String queryPart,        String sessionProperties,        String type,        boolean localOnly,        String dynamicContentProviderID,        String path,        String templateID,        String remoteURI,        String persistentProperties    ) {
        this.exists = exists;
        this.name = name;
        this.queryPart = queryPart;
        this.sessionProperties = sessionProperties;
        this.type = type;
        this.localOnly = localOnly;
        this.dynamicContentProviderID = dynamicContentProviderID;
        this.path = path;
        this.templateID = templateID;
        this.remoteURI = remoteURI;
        this.persistentProperties = persistentProperties;
    }


    public boolean getExists() {
        return exists;
    }

    public void setExists(boolean exists) {
        this.exists = exists;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQuerypart() {
        return queryPart;
    }

    public void setQuerypart(String queryPart) {
        this.queryPart = queryPart;
    }
    public String getSessionproperties() {
        return sessionProperties;
    }

    public void setSessionproperties(String sessionProperties) {
        this.sessionProperties = sessionProperties;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getLocalonly() {
        return localOnly;
    }

    public void setLocalonly(boolean localOnly) {
        this.localOnly = localOnly;
    }
    public String getDynamiccontentproviderid() {
        return dynamicContentProviderID;
    }

    public void setDynamiccontentproviderid(String dynamicContentProviderID) {
        this.dynamicContentProviderID = dynamicContentProviderID;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getTemplateid() {
        return templateID;
    }

    public void setTemplateid(String templateID) {
        this.templateID = templateID;
    }
    public String getRemoteuri() {
        return remoteURI;
    }

    public void setRemoteuri(String remoteURI) {
        this.remoteURI = remoteURI;
    }
    public String getPersistentproperties() {
        return persistentProperties;
    }

    public void setPersistentproperties(String persistentProperties) {
        this.persistentProperties = persistentProperties;
    }

    public SemanticResourceDB_ResourceTreeNode getSemanticresourcedb_resourcetreenode() {
        return semanticresourcedb_resourcetreenode;
    }

    public void setSemanticresourcedb_resourcetreenode(SemanticResourceDB_ResourceTreeNode semanticresourcedb_resourcetreenode) {
        this.semanticresourcedb_resourcetreenode = semanticresourcedb_resourcetreenode;
    }
    public SemanticResourceDB_ResourceTreeNode getSemanticresourcedb_resourcetreenode() {
        return semanticresourcedb_resourcetreenode;
    }

    public void setSemanticresourcedb_resourcetreenode(SemanticResourceDB_ResourceTreeNode semanticresourcedb_resourcetreenode) {
        this.semanticresourcedb_resourcetreenode = semanticresourcedb_resourcetreenode;
    }

}