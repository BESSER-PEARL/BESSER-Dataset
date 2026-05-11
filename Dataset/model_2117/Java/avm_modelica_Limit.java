





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_Limit  {

    private String ToleranceTimeWindow;
    private String BoundType;
    private String Notes;
    private String Name;
    private String VariableLocator;





    private modelica_avm_Value modelica_avm_value;


    public avm_modelica_Limit(
        String ToleranceTimeWindow,        String BoundType,        String Notes,        String Name,        String VariableLocator    ) {
        this.ToleranceTimeWindow = ToleranceTimeWindow;
        this.BoundType = BoundType;
        this.Notes = Notes;
        this.Name = Name;
        this.VariableLocator = VariableLocator;
    }


    public String getTolerancetimewindow() {
        return ToleranceTimeWindow;
    }

    public void setTolerancetimewindow(String ToleranceTimeWindow) {
        this.ToleranceTimeWindow = ToleranceTimeWindow;
    }
    public String getBoundtype() {
        return BoundType;
    }

    public void setBoundtype(String BoundType) {
        this.BoundType = BoundType;
    }
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getVariablelocator() {
        return VariableLocator;
    }

    public void setVariablelocator(String VariableLocator) {
        this.VariableLocator = VariableLocator;
    }

    public modelica_avm_Value getModelica_avm_value() {
        return modelica_avm_value;
    }

    public void setModelica_avm_value(modelica_avm_Value modelica_avm_value) {
        this.modelica_avm_value = modelica_avm_value;
    }

}