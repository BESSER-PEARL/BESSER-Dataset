





import java.util.List;
import java.util.ArrayList;

public class model_Throw extends Activity {

    private String faultName;





    private model_Variable model_variable;


    public model_Throw(
        String faultName    ) {
        super(
        );
        this.faultName = faultName;
    }


    public String getFaultname() {
        return faultName;
    }

    public void setFaultname(String faultName) {
        this.faultName = faultName;
    }

    public model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(model_Variable model_variable) {
        this.model_variable = model_variable;
    }

}