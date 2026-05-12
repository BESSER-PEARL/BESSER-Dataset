





import java.util.List;
import java.util.ArrayList;

public class Ant_Javac extends CompileTask {

    private String debug;
    private String deprecation;
    private String srcdir;
    private String fork;
    private String destdir;
    private String optimize;





    private ClassPath classpath;




    private List<InExcludes> inexcludess;


    public Ant_Javac(
        String debug,        String deprecation,        String srcdir,        String fork,        String destdir,        String optimize    ) {
        super(
        );
        this.debug = debug;
        this.deprecation = deprecation;
        this.srcdir = srcdir;
        this.fork = fork;
        this.destdir = destdir;
        this.optimize = optimize;
        this.inexcludess = new ArrayList<>();
    }

    public Ant_Javac(
        String debug,        String deprecation,        String srcdir,        String fork,        String destdir,        String optimize        ArrayList<InExcludes> inexcludess    ) {
        this.debug = debug;
        this.deprecation = deprecation;
        this.srcdir = srcdir;
        this.fork = fork;
        this.destdir = destdir;
        this.optimize = optimize;
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
    public String getSrcdir() {
        return srcdir;
    }

    public void setSrcdir(String srcdir) {
        this.srcdir = srcdir;
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
    public String getOptimize() {
        return optimize;
    }

    public void setOptimize(String optimize) {
        this.optimize = optimize;
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