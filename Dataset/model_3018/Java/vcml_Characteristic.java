





import java.util.List;
import java.util.ArrayList;

public class vcml_Characteristic extends VCObject {

    private boolean required;
    private boolean notReadyForInput;
    private boolean additionalValues;
    private boolean displayAllowedValues;
    private boolean restrictable;
    private boolean noDisplay;
    private String table;
    private String group;
    private String status;
    private boolean multiValue;
    private String field;





    private vcml_Class vcml_class;


    public vcml_Characteristic(
        boolean required,        boolean notReadyForInput,        boolean additionalValues,        boolean displayAllowedValues,        boolean restrictable,        boolean noDisplay,        String table,        String group,        String status,        boolean multiValue,        String field    ) {
        super(
        );
        this.required = required;
        this.notReadyForInput = notReadyForInput;
        this.additionalValues = additionalValues;
        this.displayAllowedValues = displayAllowedValues;
        this.restrictable = restrictable;
        this.noDisplay = noDisplay;
        this.table = table;
        this.group = group;
        this.status = status;
        this.multiValue = multiValue;
        this.field = field;
    }


    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public boolean getNotreadyforinput() {
        return notReadyForInput;
    }

    public void setNotreadyforinput(boolean notReadyForInput) {
        this.notReadyForInput = notReadyForInput;
    }
    public boolean getAdditionalvalues() {
        return additionalValues;
    }

    public void setAdditionalvalues(boolean additionalValues) {
        this.additionalValues = additionalValues;
    }
    public boolean getDisplayallowedvalues() {
        return displayAllowedValues;
    }

    public void setDisplayallowedvalues(boolean displayAllowedValues) {
        this.displayAllowedValues = displayAllowedValues;
    }
    public boolean getRestrictable() {
        return restrictable;
    }

    public void setRestrictable(boolean restrictable) {
        this.restrictable = restrictable;
    }
    public boolean getNodisplay() {
        return noDisplay;
    }

    public void setNodisplay(boolean noDisplay) {
        this.noDisplay = noDisplay;
    }
    public String getTable() {
        return table;
    }

    public void setTable(String table) {
        this.table = table;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public boolean getMultivalue() {
        return multiValue;
    }

    public void setMultivalue(boolean multiValue) {
        this.multiValue = multiValue;
    }
    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }

    public vcml_Class getVcml_class() {
        return vcml_class;
    }

    public void setVcml_class(vcml_Class vcml_class) {
        this.vcml_class = vcml_class;
    }

}