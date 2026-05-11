





import java.util.List;
import java.util.ArrayList;

public class fm_Attribute  {

    private String value;
    private String comment;
    private String name;
    private String id;
    private String type;
    private String description;



    public fm_Attribute(
        String value,        String comment,        String name,        String id,        String type,        String description    ) {
        this.value = value;
        this.comment = comment;
        this.name = name;
        this.id = id;
        this.type = type;
        this.description = description;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}