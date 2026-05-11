





import java.util.List;
import java.util.ArrayList;

public class robot_robot_PrintCmd extends Command {

    private String msg;
    private String line;
    private String col;
    private String duration;



    public robot_robot_PrintCmd(
        String msg,        String line,        String col,        String duration    ) {
        super(
        );
        this.msg = msg;
        this.line = line;
        this.col = col;
        this.duration = duration;
    }


    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }
    public String getLine() {
        return line;
    }

    public void setLine(String line) {
        this.line = line;
    }
    public String getCol() {
        return col;
    }

    public void setCol(String col) {
        this.col = col;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }


}