





import java.util.List;
import java.util.ArrayList;

public class minidrone_Go extends Instruction {

    private int distance;



    public minidrone_Go(
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