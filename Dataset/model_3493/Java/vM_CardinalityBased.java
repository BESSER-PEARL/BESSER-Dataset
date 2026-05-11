





import java.util.List;
import java.util.ArrayList;

public class vM_CardinalityBased extends FeaturesGroup {

    private String max;
    private String min;
    private boolean all;



    public vM_CardinalityBased(
        String max,        String min,        boolean all    ) {
        super(
        );
        this.max = max;
        this.min = min;
        this.all = all;
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
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }


}