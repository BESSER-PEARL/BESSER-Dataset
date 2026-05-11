





import java.util.List;
import java.util.ArrayList;

public class marsRover_detect_lakes  {

    private int number_of_lakes;
    private String name;
    private String lakes_colors;





    private marsRover_after_action marsrover_after_action;


    public marsRover_detect_lakes(
        int number_of_lakes,        String name,        String lakes_colors    ) {
        this.number_of_lakes = number_of_lakes;
        this.name = name;
        this.lakes_colors = lakes_colors;
    }


    public int getNumber_of_lakes() {
        return number_of_lakes;
    }

    public void setNumber_of_lakes(int number_of_lakes) {
        this.number_of_lakes = number_of_lakes;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLakes_colors() {
        return lakes_colors;
    }

    public void setLakes_colors(String lakes_colors) {
        this.lakes_colors = lakes_colors;
    }

    public marsRover_after_action getMarsrover_after_action() {
        return marsrover_after_action;
    }

    public void setMarsrover_after_action(marsRover_after_action marsrover_after_action) {
        this.marsrover_after_action = marsrover_after_action;
    }

}