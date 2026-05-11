





import java.util.List;
import java.util.ArrayList;

public class abs_Pure_exp_list  {






    private abs_Eff_expr abs_eff_expr;




    private abs_Pure_exp abs_pure_exp;




    private abs_Eff_expr abs_eff_expr;




    private abs_Pure_exp abs_pure_exp;




    private List<abs_Pure_exp> abs_pure_exps;


    public abs_Pure_exp_list(
    ) {
        this.abs_pure_exps = new ArrayList<>();
    }

    public abs_Pure_exp_list(
        ArrayList<abs_Pure_exp> abs_pure_exps    ) {
        this.abs_pure_exps = abs_pure_exps;
    }


    public abs_Eff_expr getAbs_eff_expr() {
        return abs_eff_expr;
    }

    public void setAbs_eff_expr(abs_Eff_expr abs_eff_expr) {
        this.abs_eff_expr = abs_eff_expr;
    }
    public abs_Pure_exp getAbs_pure_exp() {
        return abs_pure_exp;
    }

    public void setAbs_pure_exp(abs_Pure_exp abs_pure_exp) {
        this.abs_pure_exp = abs_pure_exp;
    }
    public abs_Eff_expr getAbs_eff_expr() {
        return abs_eff_expr;
    }

    public void setAbs_eff_expr(abs_Eff_expr abs_eff_expr) {
        this.abs_eff_expr = abs_eff_expr;
    }
    public abs_Pure_exp getAbs_pure_exp() {
        return abs_pure_exp;
    }

    public void setAbs_pure_exp(abs_Pure_exp abs_pure_exp) {
        this.abs_pure_exp = abs_pure_exp;
    }
    public List<abs_Pure_exp> getAbs_pure_exps() {
        return abs_pure_exps;
    }

    public void addAbs_pure_exp(Abs_pure_exp abs_pure_exp) {
        this.abs_pure_exps.add(abs_pure_exp);
    }

}