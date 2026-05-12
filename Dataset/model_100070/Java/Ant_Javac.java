





import java.util.List;
import java.util.ArrayList;

public class Ant_Javac extends CompileTask {

    private String deprecation;
    private String srcdir;
    private String destdir;
    private String optimize;
    private String fork;
    private String debug;





    private List<InExcludes> inexcludess;




    private ClassPath classpath;


    public Ant_Javac(
        String deprecation,        String srcdir,        String destdir,        String optimize,        String fork,        String debug    ) {
        super(
        );
        this.deprecation = deprecation;
        this.srcdir = srcdir;
        this.destdir = destdir;
        this.optimize = optimize;
        this.fork = fork;
        this.debug = debug;
        this.inexcludess = new ArrayList<>();
    }

    public Ant_Javac(
        String deprecation,        String srcdir,        String destdir,        String optimize,        String fork,        String debug        ArrayList<InExcludes> inexcludess    ) {
        this.deprecation = deprecation;
        this.srcdir = srcdir;
        this.destdir = destdir;
        this.optimize = optimize;
        this.fork = fork;
        this.debug = debug;
        this.inexcludess = inexcludess;
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