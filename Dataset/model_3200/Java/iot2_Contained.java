





import java.util.List;
import java.util.ArrayList;

public class iot2_Contained extends NamedElement {

    private String absoluteName;
    private String version;
    private String repositoryId;



    public iot2_Contained(
        String absoluteName,        String version,        String repositoryId    ) {
        super(
        );
        this.absoluteName = absoluteName;
        this.version = version;
        this.repositoryId = repositoryId;
    }


    public String getAbsolutename() {
        return absoluteName;
    }

    public void setAbsolutename(String absoluteName) {
        this.absoluteName = absoluteName;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getRepositoryid() {
        return repositoryId;
    }

    public void setRepositoryid(String repositoryId) {
        this.repositoryId = repositoryId;
    }


}