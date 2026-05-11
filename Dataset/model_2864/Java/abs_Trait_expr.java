





import java.util.List;
import java.util.ArrayList;

public class abs_Trait_expr extends Class_modifier_fragment {






    private abs_Trait_expr abs_trait_expr;




    private abs_Trait_decl abs_trait_decl;




    private abs_Method abs_method;




    private abs_Trait_decl abs_trait_decl;




    private List<abs_Method> abs_methods;


    public abs_Trait_expr(
    ) {
        super(
        );
        this.abs_methods = new ArrayList<>();
    }

    public abs_Trait_expr(
        ArrayList<abs_Method> abs_methods    ) {
        this.abs_methods = abs_methods;
    }


    public abs_Trait_expr getAbs_trait_expr() {
        return abs_trait_expr;
    }

    public void setAbs_trait_expr(abs_Trait_expr abs_trait_expr) {
        this.abs_trait_expr = abs_trait_expr;
    }
    public abs_Trait_decl getAbs_trait_decl() {
        return abs_trait_decl;
    }

    public void setAbs_trait_decl(abs_Trait_decl abs_trait_decl) {
        this.abs_trait_decl = abs_trait_decl;
    }
    public abs_Method getAbs_method() {
        return abs_method;
    }

    public void setAbs_method(abs_Method abs_method) {
        this.abs_method = abs_method;
    }
    public abs_Trait_decl getAbs_trait_decl() {
        return abs_trait_decl;
    }

    public void setAbs_trait_decl(abs_Trait_decl abs_trait_decl) {
        this.abs_trait_decl = abs_trait_decl;
    }
    public List<abs_Method> getAbs_methods() {
        return abs_methods;
    }

    public void addAbs_method(Abs_method abs_method) {
        this.abs_methods.add(abs_method);
    }

}