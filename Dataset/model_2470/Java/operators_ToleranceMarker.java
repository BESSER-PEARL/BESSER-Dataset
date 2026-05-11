





import java.util.List;
import java.util.ArrayList;

public class operators_ToleranceMarker extends Marker {

    private String direction;
    private String level;



    public operators_ToleranceMarker(
        String direction,        String level    ) {
        super(
        );
        this.direction = direction;
        this.level = level;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }


}