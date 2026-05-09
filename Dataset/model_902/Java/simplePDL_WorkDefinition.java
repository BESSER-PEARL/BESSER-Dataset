





import java.util.List;
import java.util.ArrayList;

public class simplePDL_WorkDefinition  {

    private String name;





    private simplePDL_Process simplepdl_process;


    public simplePDL_WorkDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplePDL_Process getSimplepdl_process() {
        return simplepdl_process;
    }

    public void setSimplepdl_process(simplePDL_Process simplepdl_process) {
        this.simplepdl_process = simplepdl_process;
    }

}