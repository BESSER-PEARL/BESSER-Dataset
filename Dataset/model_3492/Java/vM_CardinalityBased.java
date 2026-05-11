





import java.util.List;
import java.util.ArrayList;

public class vM_CardinalityBased extends FeaturesGroup {

    private String min;
    private boolean all;
    private String max;



    public vM_CardinalityBased(
        String min,        boolean all,        String max    ) {
        super(
        );
        this.min = min;
        this.all = all;
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
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }


}