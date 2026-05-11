





import java.util.List;
import java.util.ArrayList;

public class marsRover_indication  {

    private String name;





    private marsRover_after_action marsrover_after_action;


    public marsRover_indication(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public marsRover_after_action getMarsrover_after_action() {
        return marsrover_after_action;
    }

    public void setMarsrover_after_action(marsRover_after_action marsrover_after_action) {
        this.marsrover_after_action = marsrover_after_action;
    }

}