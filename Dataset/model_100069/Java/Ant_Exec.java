





import java.util.List;
import java.util.ArrayList;

public class Ant_Exec  {

    private String executable;
    private String dir;



    public Ant_Exec(
        String executable,        String dir    ) {
        this.executable = executable;
        this.dir = dir;
    }


    public String getExecutable() {
        return executable;
    }

    public void setExecutable(String executable) {
        this.executable = executable;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }


}