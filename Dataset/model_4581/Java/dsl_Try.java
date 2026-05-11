





import java.util.List;
import java.util.ArrayList;

public class dsl_Try  {

    private String name;





    private dsl_Process dsl_process;


    public dsl_Try(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Process getDsl_process() {
        return dsl_process;
    }

    public void setDsl_process(dsl_Process dsl_process) {
        this.dsl_process = dsl_process;
    }

}