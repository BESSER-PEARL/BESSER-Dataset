





import java.util.List;
import java.util.ArrayList;

public class platoon_ForwardCommand extends Command {

    private int distance;



    public platoon_ForwardCommand(
        int distance    ) {
        super(
        );
        this.distance = distance;
    }


    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }


}