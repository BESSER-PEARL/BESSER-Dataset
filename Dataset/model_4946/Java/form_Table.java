





import java.util.List;
import java.util.ArrayList;

public class form_Table extends AbstractTable, MultipleValuatedFormField {

    private boolean allowSelection;
    private boolean usePagination;
    private boolean selectionModeIsMultiple;





    private form_Expression form_expression;




    private form_Expression form_expression;




    private form_Expression form_expression;


    public form_Table(
        boolean allowSelection,        boolean usePagination,        boolean selectionModeIsMultiple    ) {
        super(
        );
        this.allowSelection = allowSelection;
        this.usePagination = usePagination;
        this.selectionModeIsMultiple = selectionModeIsMultiple;
    }


    public boolean getAllowselection() {
        return allowSelection;
    }

    public void setAllowselection(boolean allowSelection) {
        this.allowSelection = allowSelection;
    }
    public boolean getUsepagination() {
        return usePagination;
    }

    public void setUsepagination(boolean usePagination) {
        this.usePagination = usePagination;
    }
    public boolean getSelectionmodeismultiple() {
        return selectionModeIsMultiple;
    }

    public void setSelectionmodeismultiple(boolean selectionModeIsMultiple) {
        this.selectionModeIsMultiple = selectionModeIsMultiple;
    }

    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }
    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }
    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }

}