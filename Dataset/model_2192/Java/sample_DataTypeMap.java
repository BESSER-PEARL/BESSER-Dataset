





import java.util.List;
import java.util.ArrayList;

public class sample_DataTypeMap  {

    private String key;
    private String value;





    private sample_ETypes sample_etypes;


    public sample_DataTypeMap(
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

    public sample_ETypes getSample_etypes() {
        return sample_etypes;
    }

    public void setSample_etypes(sample_ETypes sample_etypes) {
        this.sample_etypes = sample_etypes;
    }

}