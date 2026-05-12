





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Javac extends CompileTask {

    private String destdir;
    private String deprecation;
    private String optimize;
    private String fork;
    private String srcdir;
    private String debug;





    private List<InExcludes> inexcludess;




    private ClassPath classpath;


    public MavenMaven_Javac(
        String destdir,        String deprecation,        String optimize,        String fork,        String srcdir,        String debug    ) {
        super(
        );
        this.destdir = destdir;
        this.deprecation = deprecation;
        this.optimize = optimize;
        this.fork = fork;
        this.srcdir = srcdir;
        this.debug = debug;
        this.inexcludess = new ArrayList<>();
    }

    public MavenMaven_Javac(
        String destdir,        String deprecation,        String optimize,        String fork,        String srcdir,        String debug        ArrayList<InExcludes> inexcludess    ) {
        this.destdir = destdir;
        this.deprecation = deprecation;
        this.optimize = optimize;
        this.fork = fork;
        this.srcdir = srcdir;
        this.debug = debug;
        this.inexcludess = inexcludess;
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
    public String getFork() {
        return fork;
    }

    public void setFork(String fork) {
        this.fork = fork;
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