





import java.util.List;
import java.util.ArrayList;

public class fm_FeatureModel  {

    private String comment;
    private String version;
    private String name;
    private String description;



    public fm_FeatureModel(
        String comment,        String version,        String name,        String description    ) {
        this.comment = comment;
        this.version = version;
        this.name = name;
        this.description = description;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}