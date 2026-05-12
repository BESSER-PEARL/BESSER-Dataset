





import java.util.List;
import java.util.ArrayList;

public class Ant_Java extends ExecutionTask {

    private String fork;
    private String jar;
    private String classname;



    public Ant_Java(
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


}