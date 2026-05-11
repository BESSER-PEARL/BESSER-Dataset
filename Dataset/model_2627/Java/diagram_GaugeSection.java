





import java.util.List;
import java.util.ArrayList;

public class diagram_GaugeSection extends Customizable {

    private String label;
    private String backgroundColor;
    private String min;
    private String foregroundColor;
    private String max;
    private String value;





    private diagram_GaugeCompositeStyle diagram_gaugecompositestyle;


    public diagram_GaugeSection(
        String label,        String backgroundColor,        String min,        String foregroundColor,        String max,        String value    ) {
        super(
        );
        this.label = label;
        this.backgroundColor = backgroundColor;
        this.min = min;
        this.foregroundColor = foregroundColor;
        this.max = max;
        this.value = value;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public diagram_GaugeCompositeStyle getDiagram_gaugecompositestyle() {
        return diagram_gaugecompositestyle;
    }

    public void setDiagram_gaugecompositestyle(diagram_GaugeCompositeStyle diagram_gaugecompositestyle) {
        this.diagram_gaugecompositestyle = diagram_gaugecompositestyle;
    }

}