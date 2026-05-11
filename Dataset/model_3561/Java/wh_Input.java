





import java.util.List;
import java.util.ArrayList;

public class wh_Input  {

    private String params;





    private wh_Definition wh_definition;


    public wh_Input(
        String params    ) {
        this.params = params;
    }


    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }

    public wh_Definition getWh_definition() {
        return wh_definition;
    }

    public void setWh_definition(wh_Definition wh_definition) {
        this.wh_definition = wh_definition;
    }

}