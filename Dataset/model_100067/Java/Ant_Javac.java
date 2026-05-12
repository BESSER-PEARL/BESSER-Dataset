





import java.util.List;
import java.util.ArrayList;

public class Ant_Javac extends CompileTask {

    private String optimize;
    private String fork;
    private String debug;
    private String deprecation;
    private String destdir;
    private String srcdir;





    private List<InExcludes> inexcludess;




    private ClassPath classpath;


    public Ant_Javac(
        String optimize,        String fork,        String debug,        String deprecation,        String destdir,        String srcdir    ) {
        super(
        );
        this.optimize = optimize;
        this.fork = fork;
        this.debug = debug;
        this.deprecation = deprecation;
        this.destdir = destdir;
        this.srcdir = srcdir;
        this.inexcludess = new ArrayList<>();
    }

    public Ant_Javac(
        String optimize,        String fork,        String debug,        String deprecation,        String destdir,        String srcdir        ArrayList<InExcludes> inexcludess    ) {
        this.optimize = optimize;
        this.fork = fork;
        this.debug = debug;
        this.deprecation = deprecation;
        this.destdir = destdir;
        this.srcdir = srcdir;
        this.inexcludess = inexcludess;
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
    public String getDestdir() {
        return destdir;
    }

    public void setDestdir(String destdir) {
        this.destdir = destdir;
    }
    public String getSrcdir() {
        return srcdir;
    }

    public void setSrcdir(String srcdir) {
        this.srcdir = srcdir;
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