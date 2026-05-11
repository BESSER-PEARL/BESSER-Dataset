





import java.util.List;
import java.util.ArrayList;

public class model_Property  {

    private String value;
    private String key;





    private model_Properties model_properties;


    public model_Property(
        String value,        String key    ) {
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

    public model_Properties getModel_properties() {
        return model_properties;
    }

    public void setModel_properties(model_Properties model_properties) {
        this.model_properties = model_properties;
    }

}