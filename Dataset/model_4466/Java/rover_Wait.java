





import java.util.List;
import java.util.ArrayList;

public class rover_Wait  {

    private int time;





    private rover_Command rover_command;


    public rover_Wait(
        int time    ) {
        this.time = time;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public rover_Command getRover_command() {
        return rover_command;
    }

    public void setRover_command(rover_Command rover_command) {
        this.rover_command = rover_command;
    }

}