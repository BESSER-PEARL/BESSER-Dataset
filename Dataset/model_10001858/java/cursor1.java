





import java.util.List;
import java.util.ArrayList;

public class cursor1  {

    private int pos_y;
    private String limit_y;
    private int pos_x;
    private int limit_x;



    public cursor1(
        int pos_y,        String limit_y,        int pos_x,        int limit_x    ) {
        this.pos_y = pos_y;
        this.limit_y = limit_y;
        this.pos_x = pos_x;
        this.limit_x = limit_x;
    }


    public int getPos_y() {
        return pos_y;
    }

    public void setPos_y(int pos_y) {
        this.pos_y = pos_y;
    }
    public String getLimit_y() {
        return limit_y;
    }

    public void setLimit_y(String limit_y) {
        this.limit_y = limit_y;
    }
    public int getPos_x() {
        return pos_x;
    }

    public void setPos_x(int pos_x) {
        this.pos_x = pos_x;
    }
    public int getLimit_x() {
        return limit_x;
    }

    public void setLimit_x(int limit_x) {
        this.limit_x = limit_x;
    }


}