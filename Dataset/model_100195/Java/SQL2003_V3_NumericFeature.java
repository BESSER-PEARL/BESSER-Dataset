





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_NumericFeature extends Feature {

    private String value;
    private String key;



    public SQL2003_V3_NumericFeature(
        String value,        String key    ) {
        super(
        );
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