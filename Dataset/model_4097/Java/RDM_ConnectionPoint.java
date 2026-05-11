





import java.util.List;
import java.util.ArrayList;

public class RDM_ConnectionPoint extends RDMElement {

    private String direction;



    public RDM_ConnectionPoint(
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