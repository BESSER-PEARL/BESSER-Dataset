





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Java extends ExecutionTask {

    private String classname;
    private String jar;
    private String fork;





    private ClassPath classpath;


    public MavenMaven_Java(
        String classname,        String jar,        String fork    ) {
        super(
        );
        this.classname = classname;
        this.jar = jar;
        this.fork = fork;
    }


    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }
    public String getJar() {
        return jar;
    }

    public void setJar(String jar) {
        this.jar = jar;
    }
    public String getFork() {
        return fork;
    }

    public void setFork(String fork) {
        this.fork = fork;
    }

    public ClassPath getClasspath() {
        return classpath;
    }

    public void setClasspath(ClassPath classpath) {
        this.classpath = classpath;
    }

}