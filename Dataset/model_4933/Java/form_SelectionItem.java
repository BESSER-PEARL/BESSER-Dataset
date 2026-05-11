





import java.util.List;
import java.util.ArrayList;

public class form_SelectionItem  {

    private String label;
    private boolean selected;





    private form_SelectionField form_selectionfield;




    private form_SelectionField form_selectionfield;


    public form_SelectionItem(
        String label,        boolean selected    ) {
        this.label = label;
        this.selected = selected;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }

    public form_SelectionField getForm_selectionfield() {
        return form_selectionfield;
    }

    public void setForm_selectionfield(form_SelectionField form_selectionfield) {
        this.form_selectionfield = form_selectionfield;
    }
    public form_SelectionField getForm_selectionfield() {
        return form_selectionfield;
    }

    public void setForm_selectionfield(form_SelectionField form_selectionfield) {
        this.form_selectionfield = form_selectionfield;
    }

}