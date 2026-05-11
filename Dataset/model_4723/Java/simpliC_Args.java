





import java.util.List;
import java.util.ArrayList;

public class simpliC_Args  {

    private String name;





    private simpliC_Function simplic_function;




    private simpliC_Type simplic_type;


    public simpliC_Args(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simpliC_Function getSimplic_function() {
        return simplic_function;
    }

    public void setSimplic_function(simpliC_Function simplic_function) {
        this.simplic_function = simplic_function;
    }
    public simpliC_Type getSimplic_type() {
        return simplic_type;
    }

    public void setSimplic_type(simpliC_Type simplic_type) {
        this.simplic_type = simplic_type;
    }

}