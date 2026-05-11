





import java.util.List;
import java.util.ArrayList;

public class fc_FeatureConfiguration  {

    private String description;
    private String version;
    private String comment;
    private String name;



    public fc_FeatureConfiguration(
        String description,        String version,        String comment,        String name    ) {
        this.description = description;
        this.version = version;
        this.comment = comment;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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


}