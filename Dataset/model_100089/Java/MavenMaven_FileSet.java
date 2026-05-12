





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_FileSet extends Set {

    private String dir;





    private List<Excludes> excludess;


    public MavenMaven_FileSet(
        String dir    ) {
        super(
        );
        this.dir = dir;
        this.excludess = new ArrayList<>();
    }

    public MavenMaven_FileSet(
        String dir        ArrayList<Excludes> excludess    ) {
        this.dir = dir;
        this.excludess = excludess;
    }

    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }

    public List<Excludes> getExcludess() {
        return excludess;
    }

    public void addExcludes(Excludes excludes) {
        this.excludess.add(excludes);
    }

}