





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Java extends ExecutionTask {

    private String fork;
    private String jar;
    private String classname;





    private MavenMaven_ClassPath mavenmaven_classpath;


    public MavenMaven_Java(
        String fork,        String jar,        String classname    ) {
        super(
        );
        this.fork = fork;
        this.jar = jar;
        this.classname = classname;
    }


    public String getFork() {
        return fork;
    }

    public void setFork(String fork) {
        this.fork = fork;
    }
    public String getJar() {
        return jar;
    }

    public void setJar(String jar) {
        this.jar = jar;
    }
    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }

    public MavenMaven_ClassPath getMavenmaven_classpath() {
        return mavenmaven_classpath;
    }

    public void setMavenmaven_classpath(MavenMaven_ClassPath mavenmaven_classpath) {
        this.mavenmaven_classpath = mavenmaven_classpath;
    }

}