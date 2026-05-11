





import java.util.List;
import java.util.ArrayList;

public class wh_Output  {

    private String vars;





    private wh_Definition wh_definition;


    public wh_Output(
        String vars    ) {
        this.vars = vars;
    }


    public String getVars() {
        return vars;
    }

    public void setVars(String vars) {
        this.vars = vars;
    }

    public wh_Definition getWh_definition() {
        return wh_definition;
    }

    public void setWh_definition(wh_Definition wh_definition) {
        this.wh_definition = wh_definition;
    }

}