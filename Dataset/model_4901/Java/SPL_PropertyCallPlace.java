





import java.util.List;
import java.util.ArrayList;

public class SPL_PropertyCallPlace extends VariablePlace {

    private String propName;





    private SPL_VariablePlace spl_variableplace;


    public SPL_PropertyCallPlace(
        String propName    ) {
        super(
        );
        this.propName = propName;
    }


    public String getPropname() {
        return propName;
    }

    public void setPropname(String propName) {
        this.propName = propName;
    }

    public SPL_VariablePlace getSpl_variableplace() {
        return spl_variableplace;
    }

    public void setSpl_variableplace(SPL_VariablePlace spl_variableplace) {
        this.spl_variableplace = spl_variableplace;
    }

}