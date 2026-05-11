





import java.util.List;
import java.util.ArrayList;

public class model_Property  {

    private boolean generated;
    private String value;
    private String key;



    public model_Property(
        boolean generated,        String value,        String key    ) {
        this.generated = generated;
        this.value = value;
        this.key = key;
    }


    public boolean getGenerated() {
        return generated;
    }

    public void setGenerated(boolean generated) {
        this.generated = generated;
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