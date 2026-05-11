





import java.util.List;
import java.util.ArrayList;

public class wh_Program  {

    private String name;





    private wh_Wh wh_wh;




    private wh_Definition wh_definition;


    public wh_Program(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public wh_Wh getWh_wh() {
        return wh_wh;
    }

    public void setWh_wh(wh_Wh wh_wh) {
        this.wh_wh = wh_wh;
    }
    public wh_Definition getWh_definition() {
        return wh_definition;
    }

    public void setWh_definition(wh_Definition wh_definition) {
        this.wh_definition = wh_definition;
    }

}