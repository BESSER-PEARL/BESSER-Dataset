





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_IntervalFeature extends Feature {

    private String key;
    private String value;



    public SQL2003_evo_IntervalFeature(
        String key,        String value    ) {
        super(
        );
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


}