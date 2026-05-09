





import java.util.List;
import java.util.ArrayList;

public class henshin_Annotation extends ModelElement {

    private String value;
    private String key;



    public henshin_Annotation(
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