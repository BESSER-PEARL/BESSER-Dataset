





import java.util.List;
import java.util.ArrayList;

public class hutn_Slot extends ModelElement {

    private String values;
    private String feature;



    public hutn_Slot(
        String values,        String feature    ) {
        super(
        );
        this.values = values;
        this.feature = feature;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }
    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }


}