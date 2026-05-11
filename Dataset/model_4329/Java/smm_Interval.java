





import java.util.List;
import java.util.ArrayList;

public class smm_Interval extends SmmElement {

    private float minimum;
    private String minimumOpen;
    private float maximum;
    private String maximumOpen;



    public smm_Interval(
        float minimum,        String minimumOpen,        float maximum,        String maximumOpen    ) {
        super(
        );
        this.minimum = minimum;
        this.minimumOpen = minimumOpen;
        this.maximum = maximum;
        this.maximumOpen = maximumOpen;
    }


    public float getMinimum() {
        return minimum;
    }

    public void setMinimum(float minimum) {
        this.minimum = minimum;
    }
    public String getMinimumopen() {
        return minimumOpen;
    }

    public void setMinimumopen(String minimumOpen) {
        this.minimumOpen = minimumOpen;
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


}