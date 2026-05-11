





import java.util.List;
import java.util.ArrayList;

public class taskDSL_Mission  {

    private String name;





    private taskDSL_DSL taskdsl_dsl;


    public taskDSL_Mission(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public taskDSL_DSL getTaskdsl_dsl() {
        return taskdsl_dsl;
    }

    public void setTaskdsl_dsl(taskDSL_DSL taskdsl_dsl) {
        this.taskdsl_dsl = taskdsl_dsl;
    }

}