





import java.util.List;
import java.util.ArrayList;

public class behaviour_HeadTo extends Move {

    private float direction;



    public behaviour_HeadTo(
        float direction    ) {
        super(
        );
        this.direction = direction;
    }


    public float getDirection() {
        return direction;
    }

    public void setDirection(float direction) {
        this.direction = direction;
    }


}