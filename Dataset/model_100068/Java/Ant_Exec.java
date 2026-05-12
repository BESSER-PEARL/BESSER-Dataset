





import java.util.List;
import java.util.ArrayList;

public class Ant_Exec  {

    private String dir;
    private String executable;



    public Ant_Exec(
        String dir,        String executable    ) {
        this.dir = dir;
        this.executable = executable;
    }


    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getExecutable() {
        return executable;
    }

    public void setExecutable(String executable) {
        this.executable = executable;
    }


}