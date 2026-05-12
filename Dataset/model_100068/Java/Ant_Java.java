





import java.util.List;
import java.util.ArrayList;

public class Ant_Java  {

    private String jar;
    private String fork;
    private String classname;





    private ClassPath classpath;


    public Ant_Java(
        String jar,        String fork,        String classname    ) {
        this.jar = jar;
        this.fork = fork;
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
    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }

    public ClassPath getClasspath() {
        return classpath;
    }

    public void setClasspath(ClassPath classpath) {
        this.classpath = classpath;
    }

}