





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Interval extends ValueSpecification {

    private String min;
    private String max;



    public UMLModel_Interval(
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