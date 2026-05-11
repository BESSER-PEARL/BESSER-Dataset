





import java.util.List;
import java.util.ArrayList;

public class wh_Function  {

    private String name;





    private wh_Program wh_program;


    public wh_Function(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public wh_Program getWh_program() {
        return wh_program;
    }

    public void setWh_program(wh_Program wh_program) {
        this.wh_program = wh_program;
    }

}