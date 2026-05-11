





import java.util.List;
import java.util.ArrayList;

public class feature_HyNumberAttribute extends HyFeatureAttribute {

    private int default;
    private int min;
    private int max;



    public feature_HyNumberAttribute(
        int default,        int min,        int max    ) {
        super(
        );
        this.default = default;
        this.min = min;
        this.max = max;
    }


    public int getDefault() {
        return default;
    }

    public void setDefault(int default) {
        this.default = default;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }


}