





import java.util.List;
import java.util.ArrayList;

public class marsRover_mission  {

    private String name;





    private marsRover_Robot marsrover_robot;


    public marsRover_mission(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public marsRover_Robot getMarsrover_robot() {
        return marsrover_robot;
    }

    public void setMarsrover_robot(marsRover_Robot marsrover_robot) {
        this.marsrover_robot = marsrover_robot;
    }

}