





import java.util.List;
import java.util.ArrayList;

public class roc_Direction  {

    private String LEFT;
    private String UP;
    private String DOWN;
    private String RIGHT;



    public roc_Direction(
        String LEFT,        String UP,        String DOWN,        String RIGHT    ) {
        this.LEFT = LEFT;
        this.UP = UP;
        this.DOWN = DOWN;
        this.RIGHT = RIGHT;
    }


    public String getLeft() {
        return LEFT;
    }

    public void setLeft(String LEFT) {
        this.LEFT = LEFT;
    }
    public String getUp() {
        return UP;
    }

    public void setUp(String UP) {
        this.UP = UP;
    }
    public String getDown() {
        return DOWN;
    }

    public void setDown(String DOWN) {
        this.DOWN = DOWN;
    }
    public String getRight() {
        return RIGHT;
    }

    public void setRight(String RIGHT) {
        this.RIGHT = RIGHT;
    }


}