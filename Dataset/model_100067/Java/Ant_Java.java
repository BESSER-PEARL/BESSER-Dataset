





import java.util.List;
import java.util.ArrayList;

public class Ant_Java extends ExecutionTask {

    private String fork;
    private String classname;
    private String jar;



    public Ant_Java(
        String fork,        String classname,        String jar    ) {
        super(
        );
        this.fork = fork;
        this.classname = classname;
        this.jar = jar;
    }


    public String getFork() {
        return fork;
    }

    public void setFork(String fork) {
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


}