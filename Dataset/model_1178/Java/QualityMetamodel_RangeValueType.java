





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_RangeValueType extends ValueType {

    private String max;
    private String min;



    public QualityMetamodel_RangeValueType(
        String max,        String min    ) {
        super(
        );
        this.max = max;
        this.min = min;
    }


    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }


}