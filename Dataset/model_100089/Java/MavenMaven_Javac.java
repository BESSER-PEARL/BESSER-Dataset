





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Javac extends CompileTask {

    private String debug;
    private String deprecation;
    private String optimize;
    private String srcdir;
    private String destdir;
    private String fork;





    private List<InExcludes> inexcludess;




    private ClassPath classpath;


    public MavenMaven_Javac(
        String debug,        String deprecation,        String optimize,        String srcdir,        String destdir,        String fork    ) {
        super(
        );
        this.debug = debug;
        this.deprecation = deprecation;
        this.optimize = optimize;
        this.srcdir = srcdir;
        this.destdir = destdir;
        this.fork = fork;
        this.inexcludess = new ArrayList<>();
    }

    public MavenMaven_Javac(
        String debug,        String deprecation,        String optimize,        String srcdir,        String destdir,        String fork        ArrayList<InExcludes> inexcludess    ) {
        this.debug = debug;
        this.deprecation = deprecation;
        this.optimize = optimize;
        this.srcdir = srcdir;
        this.destdir = destdir;
        this.fork = fork;
        this.inexcludess = inexcludess;
    }

    public String getDebug() {
        return debug;
    }

    public void setDebug(String debug) {
        this.debug = debug;
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

    public List<InExcludes> getInexcludess() {
        return inexcludess;
    }

    public void addInexcludes(Inexcludes inexcludes) {
        this.inexcludess.add(inexcludes);
    }
    public ClassPath getClasspath() {
        return classpath;
    }

    public void setClasspath(ClassPath classpath) {
        this.classpath = classpath;
    }

}