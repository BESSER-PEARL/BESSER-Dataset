





import java.util.List;
import java.util.ArrayList;

public class marsRover_detect_rocks  {

    private String name;
    private int number_of_rocks;





    private marsRover_after_action marsrover_after_action;


    public marsRover_detect_rocks(
        String name,        int number_of_rocks    ) {
        this.name = name;
        this.number_of_rocks = number_of_rocks;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumber_of_rocks() {
        return number_of_rocks;
    }

    public void setNumber_of_rocks(int number_of_rocks) {
        this.number_of_rocks = number_of_rocks;
    }

    public marsRover_after_action getMarsrover_after_action() {
        return marsrover_after_action;
    }

    public void setMarsrover_after_action(marsRover_after_action marsrover_after_action) {
        this.marsrover_after_action = marsrover_after_action;
    }

}