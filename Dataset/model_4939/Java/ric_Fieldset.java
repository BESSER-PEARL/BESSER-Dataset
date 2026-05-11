





import java.util.List;
import java.util.ArrayList;

public class ric_Fieldset extends IdentifiableComponent, ClassifiableComponent, EventComponent {

    private String legend;
    private String legendFormat;
    private String legendAlign;





    private ric_Div ric_div;




    private List<ric_FormControl> ric_formcontrols;


    public ric_Fieldset(
        String legend,        String legendFormat,        String legendAlign    ) {
        super(
        );
        this.legend = legend;
        this.legendFormat = legendFormat;
        this.legendAlign = legendAlign;
        this.ric_formcontrols = new ArrayList<>();
    }

    public ric_Fieldset(
        String legend,        String legendFormat,        String legendAlign        ArrayList<ric_FormControl> ric_formcontrols    ) {
        this.legend = legend;
        this.legendFormat = legendFormat;
        this.legendAlign = legendAlign;
        this.ric_formcontrols = ric_formcontrols;
    }

    public String getLegend() {
        return legend;
    }

    public void setLegend(String legend) {
        this.legend = legend;
    }
    public String getLegendformat() {
        return legendFormat;
    }

    public void setLegendformat(String legendFormat) {
        this.legendFormat = legendFormat;
    }
    public String getLegendalign() {
        return legendAlign;
    }

    public void setLegendalign(String legendAlign) {
        this.legendAlign = legendAlign;
    }

    public ric_Div getRic_div() {
        return ric_div;
    }

    public void setRic_div(ric_Div ric_div) {
        this.ric_div = ric_div;
    }
    public List<ric_FormControl> getRic_formcontrols() {
        return ric_formcontrols;
    }

    public void addRic_formcontrol(Ric_formcontrol ric_formcontrol) {
        this.ric_formcontrols.add(ric_formcontrol);
    }

}