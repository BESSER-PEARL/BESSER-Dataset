





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_IntervalFeature extends Feature {

    private String value;
    private String key;



    public ORDB4ORA_IntervalFeature(
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