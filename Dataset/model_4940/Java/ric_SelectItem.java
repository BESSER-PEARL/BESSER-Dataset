





import java.util.List;
import java.util.ArrayList;

public class ric_SelectItem  {

    private String itemLabel;
    private String value;
    private boolean selected;





    private ric_Select ric_select;


    public ric_SelectItem(
        String itemLabel,        String value,        boolean selected    ) {
        this.itemLabel = itemLabel;
        this.value = value;
        this.selected = selected;
    }


    public String getItemlabel() {
        return itemLabel;
    }

    public void setItemlabel(String itemLabel) {
        this.itemLabel = itemLabel;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }

    public ric_Select getRic_select() {
        return ric_select;
    }

    public void setRic_select(ric_Select ric_select) {
        this.ric_select = ric_select;
    }

}