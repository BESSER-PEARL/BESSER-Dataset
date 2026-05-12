





import java.util.List;
import java.util.ArrayList;

public class Ant_TaskDef  {

    private String classname;
    private String name;



    public Ant_TaskDef(
        String classname,        String name    ) {
        this.classname = classname;
        this.name = name;
    }


    public String getClassname() {
        return classname;
    }

    public void setClassname(String classname) {
        this.classname = classname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}