





import java.util.List;
import java.util.ArrayList;

public class form_DynamicTable extends AbstractTable, SingleValuatedFormField {

    private boolean allowAddRemoveColumn;
    private boolean limitMaxNumberOfColumn;
    private boolean limitMinNumberOfRow;
    private boolean limitMaxNumberOfRow;
    private boolean limitMinNumberOfColumn;
    private boolean allowAddRemoveRow;





    private form_Expression form_expression;




    private form_Expression form_expression;




    private form_Expression form_expression;




    private form_Expression form_expression;


    public form_DynamicTable(
        boolean allowAddRemoveColumn,        boolean limitMaxNumberOfColumn,        boolean limitMinNumberOfRow,        boolean limitMaxNumberOfRow,        boolean limitMinNumberOfColumn,        boolean allowAddRemoveRow    ) {
        super(
        );
        this.allowAddRemoveColumn = allowAddRemoveColumn;
        this.limitMaxNumberOfColumn = limitMaxNumberOfColumn;
        this.limitMinNumberOfRow = limitMinNumberOfRow;
        this.limitMaxNumberOfRow = limitMaxNumberOfRow;
        this.limitMinNumberOfColumn = limitMinNumberOfColumn;
        this.allowAddRemoveRow = allowAddRemoveRow;
    }


    public boolean getAllowaddremovecolumn() {
        return allowAddRemoveColumn;
    }

    public void setAllowaddremovecolumn(boolean allowAddRemoveColumn) {
        this.allowAddRemoveColumn = allowAddRemoveColumn;
    }
    public boolean getLimitmaxnumberofcolumn() {
        return limitMaxNumberOfColumn;
    }

    public void setLimitmaxnumberofcolumn(boolean limitMaxNumberOfColumn) {
        this.limitMaxNumberOfColumn = limitMaxNumberOfColumn;
    }
    public boolean getLimitminnumberofrow() {
        return limitMinNumberOfRow;
    }

    public void setLimitminnumberofrow(boolean limitMinNumberOfRow) {
        this.limitMinNumberOfRow = limitMinNumberOfRow;
    }
    public boolean getLimitmaxnumberofrow() {
        return limitMaxNumberOfRow;
    }

    public void setLimitmaxnumberofrow(boolean limitMaxNumberOfRow) {
        this.limitMaxNumberOfRow = limitMaxNumberOfRow;
    }
    public boolean getLimitminnumberofcolumn() {
        return limitMinNumberOfColumn;
    }

    public void setLimitminnumberofcolumn(boolean limitMinNumberOfColumn) {
        this.limitMinNumberOfColumn = limitMinNumberOfColumn;
    }
    public boolean getAllowaddremoverow() {
        return allowAddRemoveRow;
    }

    public void setAllowaddremoverow(boolean allowAddRemoveRow) {
        this.allowAddRemoveRow = allowAddRemoveRow;
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
    public form_Expression getForm_expression() {
        return form_expression;
    }

    public void setForm_expression(form_Expression form_expression) {
        this.form_expression = form_expression;
    }

}