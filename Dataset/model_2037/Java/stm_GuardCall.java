





import java.util.List;
import java.util.ArrayList;

public class stm_GuardCall  {

    private String parameters;





    private stm_Guard stm_guard;


    public stm_GuardCall(
        String parameters    ) {
        this.parameters = parameters;
    }


    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public stm_Guard getStm_guard() {
        return stm_guard;
    }

    public void setStm_guard(stm_Guard stm_guard) {
        this.stm_guard = stm_guard;
    }

}