





import java.util.List;
import java.util.ArrayList;

public class model_values_StringToValueMap  {

    private String key;





    private Value value;


    public model_values_StringToValueMap(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public Value getValue() {
        return value;
    }

    public void setValue(Value value) {
        this.value = value;
    }

}