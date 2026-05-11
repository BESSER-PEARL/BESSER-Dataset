





import java.util.List;
import java.util.ArrayList;

public class mm_styles_Point  {

    private int y;
    private int x;
    private int after;
    private int before;



    public mm_styles_Point(
        int y,        int x,        int after,        int before    ) {
        this.y = y;
        this.x = x;
        this.after = after;
        this.before = before;
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
    public int getAfter() {
        return after;
    }

    public void setAfter(int after) {
        this.after = after;
    }
    public int getBefore() {
        return before;
    }

    public void setBefore(int before) {
        this.before = before;
    }


}