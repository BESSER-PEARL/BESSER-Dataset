





import java.util.List;
import java.util.ArrayList;

public class simpliC_Type  {

    private String name;





    private simpliC_Function simplic_function;




    private simpliC_Decl simplic_decl;


    public simpliC_Type(
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
    public simpliC_Decl getSimplic_decl() {
        return simplic_decl;
    }

    public void setSimplic_decl(simpliC_Decl simplic_decl) {
        this.simplic_decl = simplic_decl;
    }

}