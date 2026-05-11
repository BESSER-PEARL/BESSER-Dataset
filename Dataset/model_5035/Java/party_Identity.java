





import java.util.List;
import java.util.ArrayList;

public class party_Identity  {

    private String value;
    private String type;
    private String comment;



    public party_Identity(
        String value,        String type,        String comment    ) {
        this.value = value;
        this.type = type;
        this.comment = comment;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}