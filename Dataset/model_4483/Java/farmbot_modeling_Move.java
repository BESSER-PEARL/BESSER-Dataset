





import java.util.List;
import java.util.ArrayList;

public class farmbot_modeling_Move extends SequenceCommand {

    private int y;
    private int x;
    private int speed;
    private int z;



    public farmbot_modeling_Move(
        int y,        int x,        int speed,        int z    ) {
        super(
        );
        this.y = y;
        this.x = x;
        this.speed = speed;
        this.z = z;
    }


    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
    public int getZ() {
        return z;
    }

    public void setZ(int z) {
        this.z = z;
    }


}