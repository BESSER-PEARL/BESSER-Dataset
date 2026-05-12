





import java.util.List;
import java.util.ArrayList;

public class Ant_Mkdir extends FileTask {

    private String dir;



    public Ant_Mkdir(
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