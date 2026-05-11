





import java.util.List;
import java.util.ArrayList;

public class diagram_GaugeSection extends Customizable {

    private String max;
    private String label;
    private String value;
    private String min;





    private diagram_RGBValues diagram_rgbvalues;




    private diagram_GaugeCompositeStyle diagram_gaugecompositestyle;




    private diagram_RGBValues diagram_rgbvalues;


    public diagram_GaugeSection(
        String max,        String label,        String value,        String min    ) {
        super(
        );
        this.max = max;
        this.label = label;
        this.value = value;
        this.min = min;
    }


    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
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
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }

    public diagram_RGBValues getDiagram_rgbvalues() {
        return diagram_rgbvalues;
    }

    public void setDiagram_rgbvalues(diagram_RGBValues diagram_rgbvalues) {
        this.diagram_rgbvalues = diagram_rgbvalues;
    }
    public diagram_GaugeCompositeStyle getDiagram_gaugecompositestyle() {
        return diagram_gaugecompositestyle;
    }

    public void setDiagram_gaugecompositestyle(diagram_GaugeCompositeStyle diagram_gaugecompositestyle) {
        this.diagram_gaugecompositestyle = diagram_gaugecompositestyle;
    }
    public diagram_RGBValues getDiagram_rgbvalues() {
        return diagram_rgbvalues;
    }

    public void setDiagram_rgbvalues(diagram_RGBValues diagram_rgbvalues) {
        this.diagram_rgbvalues = diagram_rgbvalues;
    }

}