





import java.util.List;
import java.util.ArrayList;

public class ric_Fieldset extends ClassifiableComponent, IdentifiableComponent, EventComponent {

    private String legend;
    private String legendAlign;
    private String legendFormat;





    private List<ric_FormControl> ric_formcontrols;




    private ric_Form ric_form;




    private ric_Div ric_div;


    public ric_Fieldset(
        String legend,        String legendAlign,        String legendFormat    ) {
        super(
        );
        this.legend = legend;
        this.legendAlign = legendAlign;
        this.legendFormat = legendFormat;
        this.ric_formcontrols = new ArrayList<>();
    }

    public ric_Fieldset(
        String legend,        String legendAlign,        String legendFormat        ArrayList<ric_FormControl> ric_formcontrols    ) {
        this.legend = legend;
        this.legendAlign = legendAlign;
        this.legendFormat = legendFormat;
        this.ric_formcontrols = ric_formcontrols;
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
    public ric_Form getRic_form() {
        return ric_form;
    }

    public void setRic_form(ric_Form ric_form) {
        this.ric_form = ric_form;
    }
    public ric_Div getRic_div() {
        return ric_div;
    }

    public void setRic_div(ric_Div ric_div) {
        this.ric_div = ric_div;
    }

}