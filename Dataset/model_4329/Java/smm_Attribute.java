





import java.util.List;
import java.util.ArrayList;

public class smm_Attribute extends SmmElement {

    private String value;
    private String tag;



    public smm_Attribute(
        String value,        String tag    ) {
        super(
        );
        this.value = value;
        this.tag = tag;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }


}