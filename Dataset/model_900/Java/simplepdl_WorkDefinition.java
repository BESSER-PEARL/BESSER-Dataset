





import java.util.List;
import java.util.ArrayList;

public class simplepdl_WorkDefinition  {

    private String name;





    private simplepdl_Process simplepdl_process;


    public simplepdl_WorkDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplepdl_Process getSimplepdl_process() {
        return simplepdl_process;
    }

    public void setSimplepdl_process(simplepdl_Process simplepdl_process) {
        this.simplepdl_process = simplepdl_process;
    }

}