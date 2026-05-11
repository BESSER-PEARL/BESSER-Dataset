





import java.util.List;
import java.util.ArrayList;

public class tym_Variable extends AbstractElement {

    private String name;
    private String vartype;





    private tym_Variable tym_variable;




    private tym_EObject tym_eobject;




    private tym_Function tym_function;


    public tym_Variable(
        String name,        String vartype    ) {
        super(
        );
        this.name = name;
        this.vartype = vartype;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVartype() {
        return vartype;
    }

    public void setVartype(String vartype) {
        this.vartype = vartype;
    }

    public tym_Variable getTym_variable() {
        return tym_variable;
    }

    public void setTym_variable(tym_Variable tym_variable) {
        this.tym_variable = tym_variable;
    }
    public tym_EObject getTym_eobject() {
        return tym_eobject;
    }

    public void setTym_eobject(tym_EObject tym_eobject) {
        this.tym_eobject = tym_eobject;
    }
    public tym_Function getTym_function() {
        return tym_function;
    }

    public void setTym_function(tym_Function tym_function) {
        this.tym_function = tym_function;
    }

}