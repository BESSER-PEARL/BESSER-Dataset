





import java.util.List;
import java.util.ArrayList;

public class build_StringProperties  {

    private String value;
    private String key;
    private boolean immutable;



    public build_StringProperties(
        String value,        String key,        boolean immutable    ) {
        this.value = value;
        this.key = key;
        this.immutable = immutable;
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
    public boolean getImmutable() {
        return immutable;
    }

    public void setImmutable(boolean immutable) {
        this.immutable = immutable;
    }


}