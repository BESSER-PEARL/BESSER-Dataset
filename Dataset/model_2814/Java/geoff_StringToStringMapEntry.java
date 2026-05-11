





import java.util.List;
import java.util.ArrayList;

public class geoff_StringToStringMapEntry  {

    private String key;
    private String value;





    private geoff_Feature geoff_feature;


    public geoff_StringToStringMapEntry(
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

    public geoff_Feature getGeoff_feature() {
        return geoff_feature;
    }

    public void setGeoff_feature(geoff_Feature geoff_feature) {
        this.geoff_feature = geoff_feature;
    }

}