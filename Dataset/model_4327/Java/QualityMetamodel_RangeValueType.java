





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_RangeValueType extends ValueType {

    private String min;
    private String max;



    public QualityMetamodel_RangeValueType(
        String min,        String max    ) {
        super(
        );
        this.min = min;
        this.max = max;
    }


    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }


}