





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Javac extends CompileTask {

    private String destdir;
    private String fork;
    private String deprecation;
    private String optimize;
    private String debug;
    private String srcdir;





    private ClassPath classpath;




    private List<InExcludes> inexcludess;


    public MavenMaven_Javac(
        String destdir,        String fork,        String deprecation,        String optimize,        String debug,        String srcdir    ) {
        super(
        );
        this.destdir = destdir;
        this.fork = fork;
        this.deprecation = deprecation;
        this.optimize = optimize;
        this.debug = debug;
        this.srcdir = srcdir;
        this.inexcludess = new ArrayList<>();
    }

    public MavenMaven_Javac(
        String destdir,        String fork,        String deprecation,        String optimize,        String debug,        String srcdir        ArrayList<InExcludes> inexcludess    ) {
        this.destdir = destdir;
        this.fork = fork;
        this.deprecation = deprecation;
        this.optimize = optimize;
        this.debug = debug;
        this.srcdir = srcdir;
        this.inexcludess = inexcludess;
    }

    public String getDestdir() {
        return destdir;
    }

    public void setDestdir(String destdir) {
        this.destdir = destdir;
    }
    public String getFork() {
        return fork;
    }

    public void setFork(String fork) {
        this.fork = fork;
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
    public String getDebug() {
        return debug;
    }

    public void setDebug(String debug) {
        this.debug = debug;
    }
    public String getSrcdir() {
        return srcdir;
    }

    public void setSrcdir(String srcdir) {
        this.srcdir = srcdir;
    }

    public ClassPath getClasspath() {
        return classpath;
    }

    public void setClasspath(ClassPath classpath) {
        this.classpath = classpath;
    }
    public List<InExcludes> getInexcludess() {
        return inexcludess;
    }

    public void addInexcludes(Inexcludes inexcludes) {
        this.inexcludess.add(inexcludes);
    }

}