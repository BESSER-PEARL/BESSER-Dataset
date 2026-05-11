





import java.util.List;
import java.util.ArrayList;

public class aadl2_DirectedFeature extends Feature {

    private String direction;



    public aadl2_DirectedFeature(
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