





import java.util.List;
import java.util.ArrayList;

public class Ant_Javac extends CompileTask {

    private String destdir;
    private String debug;
    private String fork;
    private String optimize;
    private String srcdir;
    private String deprecation;





    private ClassPath classpath;




    private List<InExcludes> inexcludess;


    public Ant_Javac(
        String destdir,        String debug,        String fork,        String optimize,        String srcdir,        String deprecation    ) {
        super(
        );
        this.destdir = destdir;
        this.debug = debug;
        this.fork = fork;
        this.optimize = optimize;
        this.srcdir = srcdir;
        this.deprecation = deprecation;
        this.inexcludess = new ArrayList<>();
    }

    public Ant_Javac(
        String destdir,        String debug,        String fork,        String optimize,        String srcdir,        String deprecation        ArrayList<InExcludes> inexcludess    ) {
        this.destdir = destdir;
        this.debug = debug;
        this.fork = fork;
        this.optimize = optimize;
        this.srcdir = srcdir;
        this.deprecation = deprecation;
        this.inexcludess = inexcludess;
    }

    public String getDestdir() {
        return destdir;
    }

    public void setDestdir(String destdir) {
        this.destdir = destdir;
    }
    public String getDebug() {
        return debug;
    }

    public void setDebug(String debug) {
        this.debug = debug;
    }
    public String getFork() {
        return fork;
    }

    public void setFork(String fork) {
        this.fork = fork;
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
    public String getDeprecation() {
        return deprecation;
    }

    public void setDeprecation(String deprecation) {
        this.deprecation = deprecation;
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