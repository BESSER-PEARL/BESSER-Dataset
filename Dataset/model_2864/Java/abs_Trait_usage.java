





import java.util.List;
import java.util.ArrayList;

public class abs_Trait_usage  {






    private List<abs_Trait_decl> abs_trait_decls;




    private abs_Class_decl abs_class_decl;


    public abs_Trait_usage(
    ) {
        this.abs_trait_decls = new ArrayList<>();
    }

    public abs_Trait_usage(
        ArrayList<abs_Trait_decl> abs_trait_decls    ) {
        this.abs_trait_decls = abs_trait_decls;
    }


    public List<abs_Trait_decl> getAbs_trait_decls() {
        return abs_trait_decls;
    }

    public void addAbs_trait_decl(Abs_trait_decl abs_trait_decl) {
        this.abs_trait_decls.add(abs_trait_decl);
    }
    public abs_Class_decl getAbs_class_decl() {
        return abs_class_decl;
    }

    public void setAbs_class_decl(abs_Class_decl abs_class_decl) {
        this.abs_class_decl = abs_class_decl;
    }

}