





import java.util.List;
import java.util.ArrayList;

public class polybot_Point  {

    private int x;
    private int y;





    private polybot_Bot polybot_bot;


    public polybot_Point(
        int x,        int y    ) {
        this.x = x;
        this.y = y;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public polybot_Bot getPolybot_bot() {
        return polybot_bot;
    }

    public void setPolybot_bot(polybot_Bot polybot_bot) {
        this.polybot_bot = polybot_bot;
    }

}