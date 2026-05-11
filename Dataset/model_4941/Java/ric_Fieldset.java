





import java.util.List;
import java.util.ArrayList;

public class ric_Fieldset extends IdentifiableComponent, EventComponent, ClassifiableComponent {

    private String legendAlign;
    private String legend;
    private String legendFormat;





    private List<ric_FormControl> ric_formcontrols;


    public ric_Fieldset(
        String legendAlign,        String legend,        String legendFormat    ) {
        super(
        );
        this.legendAlign = legendAlign;
        this.legend = legend;
        this.legendFormat = legendFormat;
        this.ric_formcontrols = new ArrayList<>();
    }

    public ric_Fieldset(
        String legendAlign,        String legend,        String legendFormat        ArrayList<ric_FormControl> ric_formcontrols    ) {
        this.legendAlign = legendAlign;
        this.legend = legend;
        this.legendFormat = legendFormat;
        this.ric_formcontrols = ric_formcontrols;
    }

    public String getLegendalign() {
        return legendAlign;
    }

    public void setLegendalign(String legendAlign) {
        this.legendAlign = legendAlign;
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

    public List<ric_FormControl> getRic_formcontrols() {
        return ric_formcontrols;
    }

    public void addRic_formcontrol(Ric_formcontrol ric_formcontrol) {
        this.ric_formcontrols.add(ric_formcontrol);
    }

}