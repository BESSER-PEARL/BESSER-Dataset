





import java.util.List;
import java.util.ArrayList;

public class diagram_GaugeSection extends Customizable {

    private String value;
    private String foregroundColor;
    private String backgroundColor;
    private String label;
    private String min;
    private String max;



    public diagram_GaugeSection(
        String value,        String foregroundColor,        String backgroundColor,        String label,        String min,        String max    ) {
        super(
        );
        this.value = value;
        this.foregroundColor = foregroundColor;
        this.backgroundColor = backgroundColor;
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