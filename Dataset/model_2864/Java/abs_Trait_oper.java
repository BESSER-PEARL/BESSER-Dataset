





import java.util.List;
import java.util.ArrayList;

public class abs_Trait_oper  {






    private abs_Trait_expr abs_trait_expr;




    private abs_Methodsig abs_methodsig;




    private List<abs_Methodsig> abs_methodsigs;




    private abs_Trait_expr abs_trait_expr;




    private abs_Trait_expr abs_trait_expr;


    public abs_Trait_oper(
    ) {
        this.abs_methodsigs = new ArrayList<>();
    }

    public abs_Trait_oper(
        ArrayList<abs_Methodsig> abs_methodsigs    ) {
        this.abs_methodsigs = abs_methodsigs;
    }


    public abs_Trait_expr getAbs_trait_expr() {
        return abs_trait_expr;
    }

    public void setAbs_trait_expr(abs_Trait_expr abs_trait_expr) {
        this.abs_trait_expr = abs_trait_expr;
    }
    public abs_Methodsig getAbs_methodsig() {
        return abs_methodsig;
    }

    public void setAbs_methodsig(abs_Methodsig abs_methodsig) {
        this.abs_methodsig = abs_methodsig;
    }
    public List<abs_Methodsig> getAbs_methodsigs() {
        return abs_methodsigs;
    }

    public void addAbs_methodsig(Abs_methodsig abs_methodsig) {
        this.abs_methodsigs.add(abs_methodsig);
    }
    public abs_Trait_expr getAbs_trait_expr() {
        return abs_trait_expr;
    }

    public void setAbs_trait_expr(abs_Trait_expr abs_trait_expr) {
        this.abs_trait_expr = abs_trait_expr;
    }
    public abs_Trait_expr getAbs_trait_expr() {
        return abs_trait_expr;
    }

    public void setAbs_trait_expr(abs_Trait_expr abs_trait_expr) {
        this.abs_trait_expr = abs_trait_expr;
    }

}