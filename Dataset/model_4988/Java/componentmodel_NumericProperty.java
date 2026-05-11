





import java.util.List;
import java.util.ArrayList;

public class componentmodel_NumericProperty extends Property {

    private float maxValue;
    private float defaultValue;
    private float minValue;



    public componentmodel_NumericProperty(
        float maxValue,        float defaultValue,        float minValue    ) {
        super(
        );
        this.maxValue = maxValue;
        this.defaultValue = defaultValue;
        this.minValue = minValue;
    }


    public float getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(float maxValue) {
        this.maxValue = maxValue;
    }
    public float getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(float defaultValue) {
        this.defaultValue = defaultValue;
    }
    public float getMinvalue() {
        return minValue;
    }

    public void setMinvalue(float minValue) {
        this.minValue = minValue;
    }


}