





import java.util.List;
import java.util.ArrayList;

public class diva_Annotation  {

    private String value;
    private String key;



    public diva_Annotation(
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


}