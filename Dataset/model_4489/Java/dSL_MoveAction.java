





import java.util.List;
import java.util.ArrayList;

public class dSL_MoveAction extends Actions {

    private String dir;



    public dSL_MoveAction(
        String dir    ) {
        super(
        );
        this.dir = dir;
    }


    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }


}