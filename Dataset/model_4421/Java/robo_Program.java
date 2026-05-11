





import java.util.List;
import java.util.ArrayList;

public class robo_Program  {

    private String name;





    private robo_Robot robo_robot;


    public robo_Program(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public robo_Robot getRobo_robot() {
        return robo_robot;
    }

    public void setRobo_robot(robo_Robot robo_robot) {
        this.robo_robot = robo_robot;
    }

}