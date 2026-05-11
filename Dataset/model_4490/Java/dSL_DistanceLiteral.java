





import java.util.List;
import java.util.ArrayList;

public class dSL_DistanceLiteral extends Expression {

    private int distance;



    public dSL_DistanceLiteral(
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