





import java.util.List;
import java.util.ArrayList;

public class domain_JavaMapper extends TypeMapper {

    private String mappedToClassName;
    private String libraryName;
    private String artifactType;
    private String groupId;
    private String artifactId;
    private String mappedToPackageName;
    private String version;



    public domain_JavaMapper(
        String mappedToClassName,        String libraryName,        String artifactType,        String groupId,        String artifactId,        String mappedToPackageName,        String version    ) {
        super(
        );
        this.mappedToClassName = mappedToClassName;
        this.libraryName = libraryName;
        this.artifactType = artifactType;
        this.groupId = groupId;
        this.artifactId = artifactId;
        this.mappedToPackageName = mappedToPackageName;
        this.version = version;
    }


    public String getMappedtoclassname() {
        return mappedToClassName;
    }

    public void setMappedtoclassname(String mappedToClassName) {
        this.mappedToClassName = mappedToClassName;
    }
    public String getLibraryname() {
        return libraryName;
    }

    public void setLibraryname(String libraryName) {
        this.libraryName = libraryName;
    }
    public String getArtifacttype() {
        return artifactType;
    }

    public void setArtifacttype(String artifactType) {
        this.artifactType = artifactType;
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
    public String getMappedtopackagename() {
        return mappedToPackageName;
    }

    public void setMappedtopackagename(String mappedToPackageName) {
        this.mappedToPackageName = mappedToPackageName;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}