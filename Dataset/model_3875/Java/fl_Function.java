





import java.util.List;
import java.util.ArrayList;

public class fl_Function  {

    private String name;





    private fl_ApplyExp fl_applyexp;




    private fl_Program fl_program;


    public fl_Function(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fl_ApplyExp getFl_applyexp() {
        return fl_applyexp;
    }

    public void setFl_applyexp(fl_ApplyExp fl_applyexp) {
        this.fl_applyexp = fl_applyexp;
    }
    public fl_Program getFl_program() {
        return fl_program;
    }

    public void setFl_program(fl_Program fl_program) {
        this.fl_program = fl_program;
    }

}