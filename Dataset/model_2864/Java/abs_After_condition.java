





import java.util.List;
import java.util.ArrayList;

public class abs_After_condition  {






    private abs_Delta_clause abs_delta_clause;




    private List<abs_Delta_decl> abs_delta_decls;


    public abs_After_condition(
    ) {
        this.abs_delta_decls = new ArrayList<>();
    }

    public abs_After_condition(
        ArrayList<abs_Delta_decl> abs_delta_decls    ) {
        this.abs_delta_decls = abs_delta_decls;
    }


    public abs_Delta_clause getAbs_delta_clause() {
        return abs_delta_clause;
    }

    public void setAbs_delta_clause(abs_Delta_clause abs_delta_clause) {
        this.abs_delta_clause = abs_delta_clause;
    }
    public List<abs_Delta_decl> getAbs_delta_decls() {
        return abs_delta_decls;
    }

    public void addAbs_delta_decl(Abs_delta_decl abs_delta_decl) {
        this.abs_delta_decls.add(abs_delta_decl);
    }

}