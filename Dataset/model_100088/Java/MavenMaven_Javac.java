





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Javac extends CompileTask {

    private String fork;
    private String destdir;
    private String deprecation;
    private String optimize;
    private String srcdir;
    private String debug;





    private MavenMaven_ClassPath mavenmaven_classpath;




    private List<MavenMaven_InExcludes> mavenmaven_inexcludess;


    public MavenMaven_Javac(
        String fork,        String destdir,        String deprecation,        String optimize,        String srcdir,        String debug    ) {
        super(
        );
        this.fork = fork;
        this.destdir = destdir;
        this.deprecation = deprecation;
        this.optimize = optimize;
        this.srcdir = srcdir;
        this.debug = debug;
        this.mavenmaven_inexcludess = new ArrayList<>();
    }

    public MavenMaven_Javac(
        String fork,        String destdir,        String deprecation,        String optimize,        String srcdir,        String debug        ArrayList<MavenMaven_InExcludes> mavenmaven_inexcludess    ) {
        this.fork = fork;
        this.destdir = destdir;
        this.deprecation = deprecation;
        this.optimize = optimize;
        this.srcdir = srcdir;
        this.debug = debug;
        this.mavenmaven_inexcludess = mavenmaven_inexcludess;
    }

    public String getFork() {
        return fork;
    }

    public void setFork(String fork) {
        this.fork = fork;
    }
    public String getDestdir() {
        return destdir;
    }

    public void setDestdir(String destdir) {
        this.destdir = destdir;
    }
    public String getDeprecation() {
        return deprecation;
    }

    public void setDeprecation(String deprecation) {
        this.deprecation = deprecation;
    }
    public String getOptimize() {
        return optimize;
    }

    public void setOptimize(String optimize) {
        this.optimize = optimize;
    }
    public String getSrcdir() {
        return srcdir;
    }

    public void setSrcdir(String srcdir) {
        this.srcdir = srcdir;
    }
    public String getDebug() {
        return debug;
    }

    public void setDebug(String debug) {
        this.debug = debug;
    }

    public MavenMaven_ClassPath getMavenmaven_classpath() {
        return mavenmaven_classpath;
    }

    public void setMavenmaven_classpath(MavenMaven_ClassPath mavenmaven_classpath) {
        this.mavenmaven_classpath = mavenmaven_classpath;
    }
    public List<MavenMaven_InExcludes> getMavenmaven_inexcludess() {
        return mavenmaven_inexcludess;
    }

    public void addMavenmaven_inexcludes(Mavenmaven_inexcludes mavenmaven_inexcludes) {
        this.mavenmaven_inexcludess.add(mavenmaven_inexcludes);
    }

}