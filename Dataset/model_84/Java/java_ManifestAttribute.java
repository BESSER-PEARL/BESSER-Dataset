





import java.util.List;
import java.util.ArrayList;

public class java_ManifestAttribute  {

    private String value;
    private String key;



    public java_ManifestAttribute(
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