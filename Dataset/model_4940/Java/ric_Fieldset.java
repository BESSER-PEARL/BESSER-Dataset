





import java.util.List;
import java.util.ArrayList;

public class ric_Fieldset extends ClassifiableComponent, EventComponent, IdentifiableComponent {

    private String legendFormat;
    private String legend;
    private String legendAlign;



    public ric_Fieldset(
        String legendFormat,        String legend,        String legendAlign    ) {
        super(
        );
        this.legendFormat = legendFormat;
        this.legend = legend;
        this.legendAlign = legendAlign;
    }


    public String getLegendformat() {
        return legendFormat;
    }

    public void setLegendformat(String legendFormat) {
        this.legendFormat = legendFormat;
    }
    public String getLegend() {
        return legend;
    }

    public void setLegend(String legend) {
        this.legend = legend;
    }
    public String getLegendalign() {
        return legendAlign;
    }

    public void setLegendalign(String legendAlign) {
        this.legendAlign = legendAlign;
    }


}