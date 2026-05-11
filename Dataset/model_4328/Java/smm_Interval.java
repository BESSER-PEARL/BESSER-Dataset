





import java.util.List;
import java.util.ArrayList;

public class smm_Interval extends SmmElement {

    private float minimum;
    private float maximum;
    private String maximumOpen;
    private String minimumOpen;



    public smm_Interval(
        float minimum,        float maximum,        String maximumOpen,        String minimumOpen    ) {
        super(
        );
        this.minimum = minimum;
        this.maximum = maximum;
        this.maximumOpen = maximumOpen;
        this.minimumOpen = minimumOpen;
    }


    public float getMinimum() {
        return minimum;
    }

    public void setMinimum(float minimum) {
        this.minimum = minimum;
    }
    public float getMaximum() {
        return maximum;
    }

    public void setMaximum(float maximum) {
        this.maximum = maximum;
    }
    public String getMaximumopen() {
        return maximumOpen;
    }

    public void setMaximumopen(String maximumOpen) {
        this.maximumOpen = maximumOpen;
    }
    public String getMinimumopen() {
        return minimumOpen;
    }

    public void setMinimumopen(String minimumOpen) {
        this.minimumOpen = minimumOpen;
    }


}