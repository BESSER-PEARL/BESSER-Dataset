





import java.util.List;
import java.util.ArrayList;

public class model_Move extends ContinuosAction, RotorAction, RandomAction {

    private String direction;



    public model_Move(
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