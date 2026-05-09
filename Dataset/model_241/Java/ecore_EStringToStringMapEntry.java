





import java.util.List;
import java.util.ArrayList;

public class ecore_EStringToStringMapEntry  {

    private String value;
    private String key;





    private ecore_EAnnotation ecore_eannotation;


    public ecore_EStringToStringMapEntry(
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

    public ecore_EAnnotation getEcore_eannotation() {
        return ecore_eannotation;
    }

    public void setEcore_eannotation(ecore_EAnnotation ecore_eannotation) {
        this.ecore_eannotation = ecore_eannotation;
    }

}