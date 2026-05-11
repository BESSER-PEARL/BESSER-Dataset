





import java.util.List;
import java.util.ArrayList;

public class model_Move extends Command {

    private String velocity;
    private int distance;



    public model_Move(
        String velocity,        int distance    ) {
        super(
        );
        this.velocity = velocity;
        this.distance = distance;
    }


    public String getVelocity() {
        return velocity;
    }

    public void setVelocity(String velocity) {
        this.velocity = velocity;
    }
    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }


}