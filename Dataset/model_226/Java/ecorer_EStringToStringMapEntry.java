





import java.util.List;
import java.util.ArrayList;

public class ecorer_EStringToStringMapEntry  {

    private String value;
    private String key;





    private ecorer_EAnnotation ecorer_eannotation;


    public ecorer_EStringToStringMapEntry(
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

    public ecorer_EAnnotation getEcorer_eannotation() {
        return ecorer_eannotation;
    }

    public void setEcorer_eannotation(ecorer_EAnnotation ecorer_eannotation) {
        this.ecorer_eannotation = ecorer_eannotation;
    }

}