





import java.util.List;
import java.util.ArrayList;

public class executionTrace_MapEntry  {

    private String key;
    private String value;



    public executionTrace_MapEntry(
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


}