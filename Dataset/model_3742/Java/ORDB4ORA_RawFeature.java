





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_RawFeature extends Feature {

    private String key;
    private String value;



    public ORDB4ORA_RawFeature(
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