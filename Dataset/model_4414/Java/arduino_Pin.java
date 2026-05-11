





import java.util.List;
import java.util.ArrayList;

public class arduino_Pin  {

    private String Direction;
    private String name;



    public arduino_Pin(
        String Direction,        String name    ) {
        this.Direction = Direction;
        this.name = name;
    }


    public String getDirection() {
        return Direction;
    }

    public void setDirection(String Direction) {
        this.Direction = Direction;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}