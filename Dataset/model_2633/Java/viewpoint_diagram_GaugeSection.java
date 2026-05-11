





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_GaugeSection extends Customizable {

    private String value;
    private String label;
    private String min;
    private String max;



    public viewpoint_diagram_GaugeSection(
        String value,        String label,        String min,        String max    ) {
        super(
        );
        this.value = value;
        this.label = label;
        this.min = min;
        this.max = max;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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