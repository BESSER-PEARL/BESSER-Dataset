





import java.util.List;
import java.util.ArrayList;

public class behaviour_GoTo extends Move {

    private String strategy;





    private behaviour_Coordinate behaviour_coordinate;


    public behaviour_GoTo(
        String strategy    ) {
        super(
        );
        this.strategy = strategy;
    }


    public String getStrategy() {
        return strategy;
    }

    public void setStrategy(String strategy) {
        this.strategy = strategy;
    }

    public behaviour_Coordinate getBehaviour_coordinate() {
        return behaviour_coordinate;
    }

    public void setBehaviour_coordinate(behaviour_Coordinate behaviour_coordinate) {
        this.behaviour_coordinate = behaviour_coordinate;
    }

}