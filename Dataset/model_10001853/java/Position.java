





import java.util.List;
import java.util.ArrayList;

public class Position  {

    private int x;
    private int y;
    private boolean has_flag;
    private boolean is_hidden;





    private MineField minefield;


    public Position(
        int x,        int y,        boolean has_flag,        boolean is_hidden    ) {
        this.x = x;
        this.y = y;
        this.has_flag = has_flag;
        this.is_hidden = is_hidden;
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
    public boolean getHas_flag() {
        return has_flag;
    }

    public void setHas_flag(boolean has_flag) {
        this.has_flag = has_flag;
    }
    public boolean getIs_hidden() {
        return is_hidden;
    }

    public void setIs_hidden(boolean is_hidden) {
        this.is_hidden = is_hidden;
    }

    public MineField getMinefield() {
        return minefield;
    }

    public void setMinefield(MineField minefield) {
        this.minefield = minefield;
    }

}