





import java.util.List;
import java.util.ArrayList;

public class ric_SelectItem  {

    private String value;
    private String itemLabel;
    private boolean selected;





    private ric_Select ric_select;


    public ric_SelectItem(
        String value,        String itemLabel,        boolean selected    ) {
        this.value = value;
        this.itemLabel = itemLabel;
        this.selected = selected;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getItemlabel() {
        return itemLabel;
    }

    public void setItemlabel(String itemLabel) {
        this.itemLabel = itemLabel;
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