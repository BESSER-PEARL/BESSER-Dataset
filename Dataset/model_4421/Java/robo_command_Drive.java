





import java.util.List;
import java.util.ArrayList;

public class robo_command_Drive extends Command {

    private String direction;



    public robo_command_Drive(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}