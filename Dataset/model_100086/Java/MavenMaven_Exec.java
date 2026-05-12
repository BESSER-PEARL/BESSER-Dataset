





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Exec extends ExecutionTask {

    private String executable;
    private String dir;



    public MavenMaven_Exec(
        String executable,        String dir    ) {
        super(
        );
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