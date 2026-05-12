





import java.util.List;
import java.util.ArrayList;

public class Ant_Javac extends CompileTask {

    private String deprecation;
    private String fork;
    private String debug;
    private String optimize;
    private String destdir;
    private String srcdir;





    private Ant_ClassPath ant_classpath;




    private List<Ant_InExcludes> ant_inexcludess;


    public Ant_Javac(
        String deprecation,        String fork,        String debug,        String optimize,        String destdir,        String srcdir    ) {
        super(
        );
        this.deprecation = deprecation;
        this.fork = fork;
        this.debug = debug;
        this.optimize = optimize;
        this.destdir = destdir;
        this.srcdir = srcdir;
        this.ant_inexcludess = new ArrayList<>();
    }

    public Ant_Javac(
        String deprecation,        String fork,        String debug,        String optimize,        String destdir,        String srcdir        ArrayList<Ant_InExcludes> ant_inexcludess    ) {
        this.deprecation = deprecation;
        this.fork = fork;
        this.debug = debug;
        this.optimize = optimize;
        this.destdir = destdir;
        this.srcdir = srcdir;
        this.ant_inexcludess = ant_inexcludess;
    }

    public String getDeprecation() {
        return deprecation;
    }

    public void setDeprecation(String deprecation) {
        this.deprecation = deprecation;
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
    public String getOptimize() {
        return optimize;
    }

    public void setOptimize(String optimize) {
        this.optimize = optimize;
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

    public Ant_ClassPath getAnt_classpath() {
        return ant_classpath;
    }

    public void setAnt_classpath(Ant_ClassPath ant_classpath) {
        this.ant_classpath = ant_classpath;
    }
    public List<Ant_InExcludes> getAnt_inexcludess() {
        return ant_inexcludess;
    }

    public void addAnt_inexcludes(Ant_inexcludes ant_inexcludes) {
        this.ant_inexcludess.add(ant_inexcludes);
    }

}