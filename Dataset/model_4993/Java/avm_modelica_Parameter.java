





import java.util.List;
import java.util.ArrayList;

public class avm_modelica_Parameter extends DomainModelParameter {

    private String Locator;





    private modelica_avm_Value modelica_avm_value;


    public avm_modelica_Parameter(
        String Locator    ) {
        super(
        );
        this.Locator = Locator;
    }


    public String getLocator() {
        return Locator;
    }

    public void setLocator(String Locator) {
        this.Locator = Locator;
    }

    public modelica_avm_Value getModelica_avm_value() {
        return modelica_avm_value;
    }

    public void setModelica_avm_value(modelica_avm_Value modelica_avm_value) {
        this.modelica_avm_value = modelica_avm_value;
    }

}