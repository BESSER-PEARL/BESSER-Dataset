





import java.util.List;
import java.util.ArrayList;

public class notation_RoundedCornersStyle extends Style {

    private int roundedBendpointsRadius;



    public notation_RoundedCornersStyle(
        int roundedBendpointsRadius    ) {
        super(
        );
        this.roundedBendpointsRadius = roundedBendpointsRadius;
    }


    public int getRoundedbendpointsradius() {
        return roundedBendpointsRadius;
    }

    public void setRoundedbendpointsradius(int roundedBendpointsRadius) {
        this.roundedBendpointsRadius = roundedBendpointsRadius;
    }


}