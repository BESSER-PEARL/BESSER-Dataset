





import java.util.List;
import java.util.ArrayList;

public class rcl_Param  {

    private String name;





    private rcl_RoverProgram rcl_roverprogram;


    public rcl_Param(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rcl_RoverProgram getRcl_roverprogram() {
        return rcl_roverprogram;
    }

    public void setRcl_roverprogram(rcl_RoverProgram rcl_roverprogram) {
        this.rcl_roverprogram = rcl_roverprogram;
    }

}