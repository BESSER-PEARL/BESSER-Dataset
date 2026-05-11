





import java.util.List;
import java.util.ArrayList;

public class mm_Property  {

    private String value;
    private String key;





    private mm_PropertyContainer mm_propertycontainer;


    public mm_Property(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public mm_PropertyContainer getMm_propertycontainer() {
        return mm_propertycontainer;
    }

    public void setMm_propertycontainer(mm_PropertyContainer mm_propertycontainer) {
        this.mm_propertycontainer = mm_propertycontainer;
    }

}