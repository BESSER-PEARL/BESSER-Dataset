





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EStringToStringMapEntry  {

    private String value;
    private String key;





    private ecoreDiff_EAnnotation ecorediff_eannotation;


    public ecoreDiff_EStringToStringMapEntry(
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

    public ecoreDiff_EAnnotation getEcorediff_eannotation() {
        return ecorediff_eannotation;
    }

    public void setEcorediff_eannotation(ecoreDiff_EAnnotation ecorediff_eannotation) {
        this.ecorediff_eannotation = ecorediff_eannotation;
    }

}