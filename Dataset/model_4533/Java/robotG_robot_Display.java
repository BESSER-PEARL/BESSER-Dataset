





import java.util.List;
import java.util.ArrayList;

public class robotG_robot_Display extends CommandeRobot {

    private String msg;
    private int duration;
    private int col;
    private int line;



    public robotG_robot_Display(
        String msg,        int duration,        int col,        int line    ) {
        super(
        );
        this.msg = msg;
        this.duration = duration;
        this.col = col;
        this.line = line;
    }


    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public int getCol() {
        return col;
    }

    public void setCol(int col) {
        this.col = col;
    }
    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }


}