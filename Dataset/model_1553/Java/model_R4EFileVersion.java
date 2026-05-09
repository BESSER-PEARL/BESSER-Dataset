





import java.util.List;
import java.util.ArrayList;

public class model_R4EFileVersion  {

    private String fileRevision;
    private String resource;
    private String versionID;
    private String localVersionID;
    private String platformURI;
    private String repositoryPath;
    private String name;





    private model_R4EAnomaly model_r4eanomaly;


    public model_R4EFileVersion(
        String fileRevision,        String resource,        String versionID,        String localVersionID,        String platformURI,        String repositoryPath,        String name    ) {
        this.fileRevision = fileRevision;
        this.resource = resource;
        this.versionID = versionID;
        this.localVersionID = localVersionID;
        this.platformURI = platformURI;
        this.repositoryPath = repositoryPath;
        this.name = name;
    }


    public String getFilerevision() {
        return fileRevision;
    }

    public void setFilerevision(String fileRevision) {
        this.fileRevision = fileRevision;
    }
    public String getResource() {
        return resource;
    }

    public void setResource(String resource) {
        this.resource = resource;
    }
    public String getVersionid() {
        return versionID;
    }

    public void setVersionid(String versionID) {
        this.versionID = versionID;
    }
    public String getLocalversionid() {
        return localVersionID;
    }

    public void setLocalversionid(String localVersionID) {
        this.localVersionID = localVersionID;
    }
    public String getPlatformuri() {
        return platformURI;
    }

    public void setPlatformuri(String platformURI) {
        this.platformURI = platformURI;
    }
    public String getRepositorypath() {
        return repositoryPath;
    }

    public void setRepositorypath(String repositoryPath) {
        this.repositoryPath = repositoryPath;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_R4EAnomaly getModel_r4eanomaly() {
        return model_r4eanomaly;
    }

    public void setModel_r4eanomaly(model_R4EAnomaly model_r4eanomaly) {
        this.model_r4eanomaly = model_r4eanomaly;
    }

}