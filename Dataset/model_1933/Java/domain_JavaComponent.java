





import java.util.List;
import java.util.ArrayList;

public class domain_JavaComponent extends Component {

    private String basePackage;
    private String version;
    private String groupId;
    private String artifactId;



    public domain_JavaComponent(
        String basePackage,        String version,        String groupId,        String artifactId    ) {
        super(
        );
        this.basePackage = basePackage;
        this.version = version;
        this.groupId = groupId;
        this.artifactId = artifactId;
    }


    public String getBasepackage() {
        return basePackage;
    }

    public void setBasepackage(String basePackage) {
        this.basePackage = basePackage;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
        this.groupId = groupId;
    }
    public String getArtifactid() {
        return artifactId;
    }

    public void setArtifactid(String artifactId) {
        this.artifactId = artifactId;
    }


}