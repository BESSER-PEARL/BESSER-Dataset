





import java.util.List;
import java.util.ArrayList;

public class abs_Type_use extends Annotation, Data_constructor_arg {

    private String name;





    private abs_Par_function_decl abs_par_function_decl;




    private abs_Function_decl abs_function_decl;




    private List<abs_Type_use> abs_type_uses;




    private abs_Typesyn_decl abs_typesyn_decl;


    public abs_Type_use(
        String name    ) {
        super(
        );
        this.name = name;
        this.abs_type_uses = new ArrayList<>();
    }

    public abs_Type_use(
        String name        ArrayList<abs_Type_use> abs_type_uses    ) {
        this.name = name;
        this.abs_type_uses = abs_type_uses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public abs_Par_function_decl getAbs_par_function_decl() {
        return abs_par_function_decl;
    }

    public void setAbs_par_function_decl(abs_Par_function_decl abs_par_function_decl) {
        this.abs_par_function_decl = abs_par_function_decl;
    }
    public abs_Function_decl getAbs_function_decl() {
        return abs_function_decl;
    }

    public void setAbs_function_decl(abs_Function_decl abs_function_decl) {
        this.abs_function_decl = abs_function_decl;
    }
    public List<abs_Type_use> getAbs_type_uses() {
        return abs_type_uses;
    }

    public void addAbs_type_use(Abs_type_use abs_type_use) {
        this.abs_type_uses.add(abs_type_use);
    }
    public abs_Typesyn_decl getAbs_typesyn_decl() {
        return abs_typesyn_decl;
    }

    public void setAbs_typesyn_decl(abs_Typesyn_decl abs_typesyn_decl) {
        this.abs_typesyn_decl = abs_typesyn_decl;
    }

}