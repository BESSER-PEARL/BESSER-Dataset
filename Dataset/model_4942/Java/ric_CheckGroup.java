





import java.util.List;
import java.util.ArrayList;

public class ric_CheckGroup  {

    private String orientation;





    private ric_Label ric_label;




    private List<ric_Checkbox> ric_checkboxs;




    private ric_Fieldset ric_fieldset;


    public ric_CheckGroup(
        String orientation    ) {
        this.orientation = orientation;
        this.ric_checkboxs = new ArrayList<>();
    }

    public ric_CheckGroup(
        String orientation        ArrayList<ric_Checkbox> ric_checkboxs    ) {
        this.orientation = orientation;
        this.ric_checkboxs = ric_checkboxs;
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
    public List<ric_Checkbox> getRic_checkboxs() {
        return ric_checkboxs;
    }

    public void addRic_checkbox(Ric_checkbox ric_checkbox) {
        this.ric_checkboxs.add(ric_checkbox);
    }
    public ric_Fieldset getRic_fieldset() {
        return ric_fieldset;
    }

    public void setRic_fieldset(ric_Fieldset ric_fieldset) {
        this.ric_fieldset = ric_fieldset;
    }

}