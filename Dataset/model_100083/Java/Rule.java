





import java.util.List;
import java.util.ArrayList;

public class Rule  {






    private Make_RuleDep make_ruledep;




    private Make_ShellLine make_shellline;


    public Rule(
    ) {
    }



    public Make_RuleDep getMake_ruledep() {
        return make_ruledep;
    }

    public void setMake_ruledep(Make_RuleDep make_ruledep) {
        this.make_ruledep = make_ruledep;
    }
    public Make_ShellLine getMake_shellline() {
        return make_shellline;
    }

    public void setMake_shellline(Make_ShellLine make_shellline) {
        this.make_shellline = make_shellline;
    }

}