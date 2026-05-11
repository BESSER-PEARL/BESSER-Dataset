





import java.util.List;
import java.util.ArrayList;

public class model_MetaData  {

    private String key;
    private String value;





    private model_Media model_media;


    public model_MetaData(
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

    public model_Media getModel_media() {
        return model_media;
    }

    public void setModel_media(model_Media model_media) {
        this.model_media = model_media;
    }

}