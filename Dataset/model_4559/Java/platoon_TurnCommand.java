





import java.util.List;
import java.util.ArrayList;

public class platoon_TurnCommand extends Command {

    private String direction;



    public platoon_TurnCommand(
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