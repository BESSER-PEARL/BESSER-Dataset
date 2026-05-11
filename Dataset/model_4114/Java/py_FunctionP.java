





import java.util.List;
import java.util.ArrayList;

public class py_FunctionP  {

    private String name;





    private py_Program py_program;


    public py_FunctionP(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public py_Program getPy_program() {
        return py_program;
    }

    public void setPy_program(py_Program py_program) {
        this.py_program = py_program;
    }

}