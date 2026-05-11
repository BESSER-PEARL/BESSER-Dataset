





import java.util.List;
import java.util.ArrayList;

public class pyrep_MoveCollection extends Entity {

    private String name;
    private boolean concurrent;





    private pyrep_Robot pyrep_robot;




    private pyrep_Environment pyrep_environment;


    public pyrep_MoveCollection(
        String name,        boolean concurrent    ) {
        super(
        );
        this.name = name;
        this.concurrent = concurrent;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getConcurrent() {
        return concurrent;
    }

    public void setConcurrent(boolean concurrent) {
        this.concurrent = concurrent;
    }

    public pyrep_Robot getPyrep_robot() {
        return pyrep_robot;
    }

    public void setPyrep_robot(pyrep_Robot pyrep_robot) {
        this.pyrep_robot = pyrep_robot;
    }
    public pyrep_Environment getPyrep_environment() {
        return pyrep_environment;
    }

    public void setPyrep_environment(pyrep_Environment pyrep_environment) {
        this.pyrep_environment = pyrep_environment;
    }

}