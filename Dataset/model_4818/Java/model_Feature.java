





import java.util.List;
import java.util.ArrayList;

public class model_Feature  {

    private String value;
    private String name;





    private model_Features model_features;


    public model_Feature(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Features getModel_features() {
        return model_features;
    }

    public void setModel_features(model_Features model_features) {
        this.model_features = model_features;
    }

}