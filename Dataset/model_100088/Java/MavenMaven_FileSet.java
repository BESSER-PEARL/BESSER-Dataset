





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_FileSet extends Set {

    private String dir;





    private MavenMaven_Path mavenmaven_path;




    private MavenMaven_ClassPath mavenmaven_classpath;




    private List<MavenMaven_PatternSet> mavenmaven_patternsets;


    public MavenMaven_FileSet(
        String dir    ) {
        super(
        );
        this.dir = dir;
        this.mavenmaven_patternsets = new ArrayList<>();
    }

    public MavenMaven_FileSet(
        String dir        ArrayList<MavenMaven_PatternSet> mavenmaven_patternsets    ) {
        this.dir = dir;
        this.mavenmaven_patternsets = mavenmaven_patternsets;
    }

    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }

    public MavenMaven_Path getMavenmaven_path() {
        return mavenmaven_path;
    }

    public void setMavenmaven_path(MavenMaven_Path mavenmaven_path) {
        this.mavenmaven_path = mavenmaven_path;
    }
    public MavenMaven_ClassPath getMavenmaven_classpath() {
        return mavenmaven_classpath;
    }

    public void setMavenmaven_classpath(MavenMaven_ClassPath mavenmaven_classpath) {
        this.mavenmaven_classpath = mavenmaven_classpath;
    }
    public List<MavenMaven_PatternSet> getMavenmaven_patternsets() {
        return mavenmaven_patternsets;
    }

    public void addMavenmaven_patternset(Mavenmaven_patternset mavenmaven_patternset) {
        this.mavenmaven_patternsets.add(mavenmaven_patternset);
    }

}