





import java.util.List;
import java.util.ArrayList;

public class polybot_modelling_language_MoveStraight extends Instruction {

    private int distance;



    public polybot_modelling_language_MoveStraight(
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