





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Point  {

    private int before;
    private int after;
    private int y;
    private int x;



    public mm_styles_Point(
        int before,        int after,        int y,        int x    ) {
        this.before = before;
        this.after = after;
        this.y = y;
        this.x = x;
    }


    public int getBefore() {
        return before;
    }

    public void setBefore(int before) {
        this.before = before;
    }
    public int getAfter() {
        return after;
    }

    public void setAfter(int after) {
        this.after = after;
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


}