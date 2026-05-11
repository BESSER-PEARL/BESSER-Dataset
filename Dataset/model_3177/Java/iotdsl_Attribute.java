





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Attribute  {

    private String value;
    private String typeName;
    private String tag;



    public iotdsl_Attribute(
        String value,        String typeName,        String tag    ) {
        this.value = value;
        this.typeName = typeName;
        this.tag = tag;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }


}