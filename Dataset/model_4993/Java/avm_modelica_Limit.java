





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_Limit  {

    private String BoundType;
    private String ToleranceTimeWindow;
    private String Notes;
    private String VariableLocator;
    private String Name;





    private modelica_avm_Value modelica_avm_value;


    public avm_modelica_Limit(
        String BoundType,        String ToleranceTimeWindow,        String Notes,        String VariableLocator,        String Name    ) {
        this.BoundType = BoundType;
        this.ToleranceTimeWindow = ToleranceTimeWindow;
        this.Notes = Notes;
        this.VariableLocator = VariableLocator;
        this.Name = Name;
    }


    public String getBoundtype() {
        return BoundType;
    }

    public void setBoundtype(String BoundType) {
        this.BoundType = BoundType;
    }
    public String getTolerancetimewindow() {
        return ToleranceTimeWindow;
    }

    public void setTolerancetimewindow(String ToleranceTimeWindow) {
        this.ToleranceTimeWindow = ToleranceTimeWindow;
    }
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }
    public String getVariablelocator() {
        return VariableLocator;
    }

    public void setVariablelocator(String VariableLocator) {
        this.VariableLocator = VariableLocator;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public modelica_avm_Value getModelica_avm_value() {
        return modelica_avm_value;
    }

    public void setModelica_avm_value(modelica_avm_Value modelica_avm_value) {
        this.modelica_avm_value = modelica_avm_value;
    }

}