





import java.util.List;
import java.util.ArrayList;

public class rcl_ObstacleQuery extends BooleanValue, Query {

    private boolean front;



    public rcl_ObstacleQuery(
        boolean front    ) {
        super(
        );
        this.front = front;
    }


    public boolean getFront() {
        return front;
    }

    public void setFront(boolean front) {
        this.front = front;
    }


}