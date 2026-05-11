





import java.util.List;
import java.util.ArrayList;

public class rover_Move  {

    private int length;
    private int velocity;





    private rover_Command rover_command;


    public rover_Move(
        int length,        int velocity    ) {
        this.length = length;
        this.velocity = velocity;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public int getVelocity() {
        return velocity;
    }

    public void setVelocity(int velocity) {
        this.velocity = velocity;
    }

    public rover_Command getRover_command() {
        return rover_command;
    }

    public void setRover_command(rover_Command rover_command) {
        this.rover_command = rover_command;
    }

}