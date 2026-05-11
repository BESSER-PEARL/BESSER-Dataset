





import java.util.List;
import java.util.ArrayList;

public class SemanticResourceDB_ResourceTreeNode  {

    private boolean exists;
    private String queryPart;
    private String dynamicContentProviderID;
    private String path;
    private String templateID;
    private String persistentProperties;
    private String remoteURI;
    private boolean localOnly;
    private String name;
    private String type;
    private String sessionProperties;





    private SemanticResourceDB_ResourceTreeNode semanticresourcedb_resourcetreenode;




    private SemanticResourceDB_ResourceTreeNode semanticresourcedb_resourcetreenode;


    public SemanticResourceDB_ResourceTreeNode(
        boolean exists,        String queryPart,        String dynamicContentProviderID,        String path,        String templateID,        String persistentProperties,        String remoteURI,        boolean localOnly,        String name,        String type,        String sessionProperties    ) {
        this.exists = exists;
        this.queryPart = queryPart;
        this.dynamicContentProviderID = dynamicContentProviderID;
        this.path = path;
        this.templateID = templateID;
        this.persistentProperties = persistentProperties;
        this.remoteURI = remoteURI;
        this.localOnly = localOnly;
        this.name = name;
        this.type = type;
        this.sessionProperties = sessionProperties;
    }


    public boolean getExists() {
        return exists;
    }

    public void setExists(boolean exists) {
        this.exists = exists;
    }
    public String getQuerypart() {
        return queryPart;
    }

    public void setQuerypart(String queryPart) {
        this.queryPart = queryPart;
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
    public String getPersistentproperties() {
        return persistentProperties;
    }

    public void setPersistentproperties(String persistentProperties) {
        this.persistentProperties = persistentProperties;
    }
    public String getRemoteuri() {
        return remoteURI;
    }

    public void setRemoteuri(String remoteURI) {
        this.remoteURI = remoteURI;
    }
    public boolean getLocalonly() {
        return localOnly;
    }

    public void setLocalonly(boolean localOnly) {
        this.localOnly = localOnly;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSessionproperties() {
        return sessionProperties;
    }

    public void setSessionproperties(String sessionProperties) {
        this.sessionProperties = sessionProperties;
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