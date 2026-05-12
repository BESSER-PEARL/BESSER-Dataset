





import java.util.List;
import java.util.ArrayList;

public class Ant_Javac extends CompileTask {

    private String deprecation;
    private String destdir;
    private String optimize;
    private String srcdir;
    private String debug;
    private String fork;





    private List<InExcludes> inexcludess;




    private ClassPath classpath;


    public Ant_Javac(
        String deprecation,        String destdir,        String optimize,        String srcdir,        String debug,        String fork    ) {
        super(
        );
        this.deprecation = deprecation;
        this.destdir = destdir;
        this.optimize = optimize;
        this.srcdir = srcdir;
        this.debug = debug;
        this.fork = fork;
        this.inexcludess = new ArrayList<>();
    }

    public Ant_Javac(
        String deprecation,        String destdir,        String optimize,        String srcdir,        String debug,        String fork        ArrayList<InExcludes> inexcludess    ) {
        this.deprecation = deprecation;
        this.destdir = destdir;
        this.optimize = optimize;
        this.srcdir = srcdir;
        this.debug = debug;
        this.fork = fork;
        this.inexcludess = inexcludess;
    }

    public String getDeprecation() {
        return deprecation;
    }

    public void setDeprecation(String deprecation) {
        this.deprecation = deprecation;
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