





import java.util.List;
import java.util.ArrayList;

public class smm_Attribute extends SmmElement {

    private String tag;
    private String value;



    public smm_Attribute(
        String tag,        String value    ) {
        super(
        );
        this.tag = tag;
        this.value = value;
    }


    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}