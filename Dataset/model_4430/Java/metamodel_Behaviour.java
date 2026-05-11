





import java.util.List;
import java.util.ArrayList;

public class metamodel_Behaviour  {

    private String name;
    private int priority;





    private metamodel_Robot metamodel_robot;


    public metamodel_Behaviour(
        String name,        int priority    ) {
        this.name = name;
        this.priority = priority;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public metamodel_Robot getMetamodel_robot() {
        return metamodel_robot;
    }

    public void setMetamodel_robot(metamodel_Robot metamodel_robot) {
        this.metamodel_robot = metamodel_robot;
    }

}