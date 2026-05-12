





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_FileList extends Basic {

    private String dir;
    private String files;



    public MavenMaven_FileList(
        String dir,        String files    ) {
        super(
        );
        this.dir = dir;
        this.files = files;
    }


    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }
    public String getFiles() {
        return files;
    }

    public void setFiles(String files) {
        this.files = files;
    }


}