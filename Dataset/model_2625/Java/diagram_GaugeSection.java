





import java.util.List;
import java.util.ArrayList;

public class diagram_GaugeSection extends Customizable {

    private String min;
    private String label;
    private String value;
    private String max;
    private String foregroundColor;
    private String backgroundColor;



    public diagram_GaugeSection(
        String min,        String label,        String value,        String max,        String foregroundColor,        String backgroundColor    ) {
        super(
        );
        this.min = min;
        this.label = label;
        this.value = value;
        this.max = max;
        this.foregroundColor = foregroundColor;
        this.backgroundColor = backgroundColor;
    }


    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }


}