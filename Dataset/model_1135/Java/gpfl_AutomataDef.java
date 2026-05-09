





import java.util.List;
import java.util.ArrayList;

public class gpfl_AutomataDef  {

    private String name;





    private gpfl_Program gpfl_program;


    public gpfl_AutomataDef(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gpfl_Program getGpfl_program() {
        return gpfl_program;
    }

    public void setGpfl_program(gpfl_Program gpfl_program) {
        this.gpfl_program = gpfl_program;
    }

}