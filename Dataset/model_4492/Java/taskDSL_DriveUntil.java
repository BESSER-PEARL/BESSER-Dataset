





import java.util.List;
import java.util.ArrayList;

public class taskDSL_DriveUntil extends Action {

    private String color;
    private String speed;
    private String object;



    public taskDSL_DriveUntil(
        String color,        String speed,        String object    ) {
        super(
        );
        this.color = color;
        this.speed = speed;
        this.object = object;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }
    public String getObject() {
        return object;
    }

    public void setObject(String object) {
        this.object = object;
    }


}