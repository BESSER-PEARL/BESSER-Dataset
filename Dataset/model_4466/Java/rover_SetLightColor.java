





import java.util.List;
import java.util.ArrayList;

public class rover_SetLightColor  {

    private String color;





    private rover_Command rover_command;


    public rover_SetLightColor(
        String color    ) {
        this.color = color;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public rover_Command getRover_command() {
        return rover_command;
    }

    public void setRover_command(rover_Command rover_command) {
        this.rover_command = rover_command;
    }

}