





import java.util.List;
import java.util.ArrayList;

public class operators_ToleranceMarker extends Marker {

    private String level;
    private String direction;



    public operators_ToleranceMarker(
        String level,        String direction    ) {
        super(
        );
        this.level = level;
        this.direction = direction;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }


}