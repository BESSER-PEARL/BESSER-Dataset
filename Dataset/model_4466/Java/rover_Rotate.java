





import java.util.List;
import java.util.ArrayList;

public class rover_Rotate  {

    private int angel;





    private rover_Command rover_command;


    public rover_Rotate(
        int angel    ) {
        this.angel = angel;
    }


    public int getAngel() {
        return angel;
    }

    public void setAngel(int angel) {
        this.angel = angel;
    }

    public rover_Command getRover_command() {
        return rover_command;
    }

    public void setRover_command(rover_Command rover_command) {
        this.rover_command = rover_command;
    }

}