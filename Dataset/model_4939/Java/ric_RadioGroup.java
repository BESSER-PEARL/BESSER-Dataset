





import java.util.List;
import java.util.ArrayList;

public class ric_RadioGroup  {

    private String orientation;





    private ric_Label ric_label;




    private ric_Fieldset ric_fieldset;




    private List<ric_Radio> ric_radios;


    public ric_RadioGroup(
        String orientation    ) {
        this.orientation = orientation;
        this.ric_radios = new ArrayList<>();
    }

    public ric_RadioGroup(
        String orientation        ArrayList<ric_Radio> ric_radios    ) {
        this.orientation = orientation;
        this.ric_radios = ric_radios;
    }

    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }

    public ric_Label getRic_label() {
        return ric_label;
    }

    public void setRic_label(ric_Label ric_label) {
        this.ric_label = ric_label;
    }
    public ric_Fieldset getRic_fieldset() {
        return ric_fieldset;
    }

    public void setRic_fieldset(ric_Fieldset ric_fieldset) {
        this.ric_fieldset = ric_fieldset;
    }
    public List<ric_Radio> getRic_radios() {
        return ric_radios;
    }

    public void addRic_radio(Ric_radio ric_radio) {
        this.ric_radios.add(ric_radio);
    }

}