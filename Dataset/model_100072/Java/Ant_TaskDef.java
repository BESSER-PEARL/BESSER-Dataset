





import java.util.List;
import java.util.ArrayList;

public class Ant_TaskDef  {

    private String name;
    private String classname;



    public Ant_TaskDef(
        String name,        String classname    ) {
        this.name = name;
        this.classname = classname;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }


}