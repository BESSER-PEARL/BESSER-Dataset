





import java.util.List;
import java.util.ArrayList;

public class wh_Vars  {

    private String variables;





    private wh_Assign wh_assign;


    public wh_Vars(
        String variables    ) {
        this.variables = variables;
    }


    public String getVariables() {
        return variables;
    }

    public void setVariables(String variables) {
        this.variables = variables;
    }

    public wh_Assign getWh_assign() {
        return wh_assign;
    }

    public void setWh_assign(wh_Assign wh_assign) {
        this.wh_assign = wh_assign;
    }

}