





import java.util.List;
import java.util.ArrayList;

public class py_Input  {

    private String vars;





    private py_Definition py_definition;


    public py_Input(
        String vars    ) {
        this.vars = vars;
    }


    public String getVars() {
        return vars;
    }

    public void setVars(String vars) {
        this.vars = vars;
    }

    public py_Definition getPy_definition() {
        return py_definition;
    }

    public void setPy_definition(py_Definition py_definition) {
        this.py_definition = py_definition;
    }

}