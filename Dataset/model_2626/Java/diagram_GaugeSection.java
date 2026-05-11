





import java.util.List;
import java.util.ArrayList;

public class diagram_GaugeSection extends Customizable {

    private String max;
    private String backgroundColor;
    private String foregroundColor;
    private String min;
    private String value;
    private String label;





    private diagram_GaugeCompositeStyle diagram_gaugecompositestyle;


    public diagram_GaugeSection(
        String max,        String backgroundColor,        String foregroundColor,        String min,        String value,        String label    ) {
        super(
        );
        this.max = max;
        this.backgroundColor = backgroundColor;
        this.foregroundColor = foregroundColor;
        this.min = min;
        this.value = value;
        this.label = label;
    }


    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getForegroundcolor() {
        return foregroundColor;
    }

    public void setForegroundcolor(String foregroundColor) {
        this.foregroundColor = foregroundColor;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
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

    public diagram_GaugeCompositeStyle getDiagram_gaugecompositestyle() {
        return diagram_gaugecompositestyle;
    }

    public void setDiagram_gaugecompositestyle(diagram_GaugeCompositeStyle diagram_gaugecompositestyle) {
        this.diagram_gaugecompositestyle = diagram_gaugecompositestyle;
    }

}