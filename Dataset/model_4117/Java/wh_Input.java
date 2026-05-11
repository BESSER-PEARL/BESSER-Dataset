





import java.util.List;
import java.util.ArrayList;

public class wh_Input  {

    private String variable;





    private wh_Definition wh_definition;




    private wh_Input wh_input;


    public wh_Input(
        String variable    ) {
        this.variable = variable;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public wh_Definition getWh_definition() {
        return wh_definition;
    }

    public void setWh_definition(wh_Definition wh_definition) {
        this.wh_definition = wh_definition;
    }
    public wh_Input getWh_input() {
        return wh_input;
    }

    public void setWh_input(wh_Input wh_input) {
        this.wh_input = wh_input;
    }

}