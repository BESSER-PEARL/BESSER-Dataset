





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Exec extends ExecutionTask {

    private String dir;
    private String executable;



    public MavenMaven_Exec(
        String dir,        String executable    ) {
        super(
        );
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