





import java.util.List;
import java.util.ArrayList;

public class presentation_AbstractComboBoxCellEditor extends CellEditor {

    private String activationStyle;



    public presentation_AbstractComboBoxCellEditor(
        String activationStyle    ) {
        super(
        );
        this.activationStyle = activationStyle;
    }


    public String getActivationstyle() {
        return activationStyle;
    }

    public void setActivationstyle(String activationStyle) {
        this.activationStyle = activationStyle;
    }


}