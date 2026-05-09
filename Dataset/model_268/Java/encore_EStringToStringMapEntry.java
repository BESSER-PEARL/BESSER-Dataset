





import java.util.List;
import java.util.ArrayList;

public class encore_EStringToStringMapEntry  {

    private String key;
    private String value;





    private encore_EAnnotation encore_eannotation;


    public encore_EStringToStringMapEntry(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public encore_EAnnotation getEncore_eannotation() {
        return encore_eannotation;
    }

    public void setEncore_eannotation(encore_EAnnotation encore_eannotation) {
        this.encore_eannotation = encore_eannotation;
    }

}