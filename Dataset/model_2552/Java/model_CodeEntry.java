





import java.util.List;
import java.util.ArrayList;

public class model_CodeEntry  {

    private String value;
    private String id;
    private String key;



    public model_CodeEntry(
        String value,        String id,        String key    ) {
        this.value = value;
        this.id = id;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}