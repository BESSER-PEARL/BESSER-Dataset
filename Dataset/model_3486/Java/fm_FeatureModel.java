





import java.util.List;
import java.util.ArrayList;

public class fm_FeatureModel  {

    private String description;
    private String comment;
    private String name;
    private String version;



    public fm_FeatureModel(
        String description,        String comment,        String name,        String version    ) {
        this.description = description;
        this.comment = comment;
        this.name = name;
        this.version = version;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}