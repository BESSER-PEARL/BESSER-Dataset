





import java.util.List;
import java.util.ArrayList;

public class cjsidl_valueSpec  {

    private String comment;
    private String name;
    private String value;



    public cjsidl_valueSpec(
        String comment,        String name,        String value    ) {
        this.comment = comment;
        this.name = name;
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
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}