





import java.util.List;
import java.util.ArrayList;

public class ecoreO_EStringToStringMapEntry  {

    private String value;
    private String key;





    private ecoreO_EAnnotation ecoreo_eannotation;


    public ecoreO_EStringToStringMapEntry(
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

    public ecoreO_EAnnotation getEcoreo_eannotation() {
        return ecoreo_eannotation;
    }

    public void setEcoreo_eannotation(ecoreO_EAnnotation ecoreo_eannotation) {
        this.ecoreo_eannotation = ecoreo_eannotation;
    }

}