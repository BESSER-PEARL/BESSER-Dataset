





import java.util.List;
import java.util.ArrayList;

public class Ant_FileList extends Basic {

    private String files;
    private String dir;



    public Ant_FileList(
        String files,        String dir    ) {
        super(
        );
        this.files = files;
        this.dir = dir;
    }


    public String getFiles() {
        return files;
    }

    public void setFiles(String files) {
        this.files = files;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }


}