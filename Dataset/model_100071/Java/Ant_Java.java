





import java.util.List;
import java.util.ArrayList;

public class Ant_Java extends ExecutionTask {

    private String jar;
    private String classname;
    private String fork;





    private Ant_ClassPath ant_classpath;


    public Ant_Java(
        String jar,        String classname,        String fork    ) {
        super(
        );
        this.jar = jar;
        this.classname = classname;
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
    public String getFork() {
        return fork;
    }

    public void setFork(String fork) {
        this.fork = fork;
    }

    public Ant_ClassPath getAnt_classpath() {
        return ant_classpath;
    }

    public void setAnt_classpath(Ant_ClassPath ant_classpath) {
        this.ant_classpath = ant_classpath;
    }

}