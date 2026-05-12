





import java.util.List;
import java.util.ArrayList;

public class MavenProject_Project  {

    private String groupId;
    private String description;
    private String artifactId;
    private String name;
    private String id;



    public MavenProject_Project(
        String groupId,        String description,        String artifactId,        String name,        String id    ) {
        this.groupId = groupId;
        this.description = description;
        this.artifactId = artifactId;
        this.name = name;
        this.id = id;
    }


    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
        this.groupId = groupId;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getArtifactid() {
        return artifactId;
    }

    public void setArtifactid(String artifactId) {
        this.artifactId = artifactId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}