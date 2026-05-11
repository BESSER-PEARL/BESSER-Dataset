





import java.util.List;
import java.util.ArrayList;

public class diagram_GaugeSection extends Customizable {

    private String label;
    private String foregroundColor;
    private String value;
    private String min;
    private String backgroundColor;
    private String max;





    private diagram_GaugeCompositeStyle diagram_gaugecompositestyle;


    public diagram_GaugeSection(
        String label,        String foregroundColor,        String value,        String min,        String backgroundColor,        String max    ) {
        super(
        );
        this.label = label;
        this.foregroundColor = foregroundColor;
        this.value = value;
        this.min = min;
        this.backgroundColor = backgroundColor;
        this.max = max;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }

    public diagram_GaugeCompositeStyle getDiagram_gaugecompositestyle() {
        return diagram_gaugecompositestyle;
    }

    public void setDiagram_gaugecompositestyle(diagram_GaugeCompositeStyle diagram_gaugecompositestyle) {
        this.diagram_gaugecompositestyle = diagram_gaugecompositestyle;
    }

}