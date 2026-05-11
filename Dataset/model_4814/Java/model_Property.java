





import java.util.List;
import java.util.ArrayList;

public class model_Property  {

    private String value;
    private String key;





    private model_Metadata model_metadata;


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

    public model_Metadata getModel_metadata() {
        return model_metadata;
    }

    public void setModel_metadata(model_Metadata model_metadata) {
        this.model_metadata = model_metadata;
    }

}