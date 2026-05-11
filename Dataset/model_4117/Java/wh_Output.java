





import java.util.List;
import java.util.ArrayList;

public class wh_Output  {

    private String variable;





    private wh_Output wh_output;




    private wh_Definition wh_definition;


    public wh_Output(
        String variable    ) {
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public wh_Output getWh_output() {
        return wh_output;
    }

    public void setWh_output(wh_Output wh_output) {
        this.wh_output = wh_output;
    }
    public wh_Definition getWh_definition() {
        return wh_definition;
    }

    public void setWh_definition(wh_Definition wh_definition) {
        this.wh_definition = wh_definition;
    }

}