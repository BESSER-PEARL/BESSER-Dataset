





import java.util.List;
import java.util.ArrayList;

public class fm_Attribute  {

    private String description;
    private String type;
    private String name;
    private String id;
    private String comment;
    private String defaultValue;





    private fm_Feature fm_feature;




    private fm_Feature fm_feature;


    public fm_Attribute(
        String description,        String type,        String name,        String id,        String comment,        String defaultValue    ) {
        this.description = description;
        this.type = type;
        this.name = name;
        this.id = id;
        this.comment = comment;
        this.defaultValue = defaultValue;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }
    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }

}