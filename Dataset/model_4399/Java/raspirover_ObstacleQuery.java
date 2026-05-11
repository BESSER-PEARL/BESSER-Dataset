





import java.util.List;
import java.util.ArrayList;

public class raspirover_ObstacleQuery extends Query, BooleanValue {

    private boolean front;



    public raspirover_ObstacleQuery(
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