





import java.util.List;
import java.util.ArrayList;

public class wh_Function  {

    private String fname;





    private wh_Program wh_program;


    public wh_Function(
        String fname    ) {
        this.fname = fname;
    }


    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }

    public wh_Program getWh_program() {
        return wh_program;
    }

    public void setWh_program(wh_Program wh_program) {
        this.wh_program = wh_program;
    }

}