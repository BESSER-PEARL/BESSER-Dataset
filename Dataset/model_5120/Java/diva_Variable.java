





import java.util.List;
import java.util.ArrayList;

public class diva_Variable extends NamedElement {






    private diva_VariableValue diva_variablevalue;




    private diva_VariabilityModel diva_variabilitymodel;


    public diva_Variable(
    ) {
        super(
        );
    }



    public diva_VariableValue getDiva_variablevalue() {
        return diva_variablevalue;
    }

    public void setDiva_variablevalue(diva_VariableValue diva_variablevalue) {
        this.diva_variablevalue = diva_variablevalue;
    }
    public diva_VariabilityModel getDiva_variabilitymodel() {
        return diva_variabilitymodel;
    }

    public void setDiva_variabilitymodel(diva_VariabilityModel diva_variabilitymodel) {
        this.diva_variabilitymodel = diva_variabilitymodel;
    }

}