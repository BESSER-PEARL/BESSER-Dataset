





import java.util.List;
import java.util.ArrayList;

public class fM_Var extends Formula {

    private boolean not_;
    private String name;





    private fM_RuleElement fm_ruleelement;




    private fM_RuleElement fm_ruleelement;


    public fM_Var(
        boolean not_,        String name    ) {
        super(
        );
        this.not_ = not_;
        this.name = name;
    }


    public boolean getNot_() {
        return not_;
    }

    public void setNot_(boolean not_) {
        this.not_ = not_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fM_RuleElement getFm_ruleelement() {
        return fm_ruleelement;
    }

    public void setFm_ruleelement(fM_RuleElement fm_ruleelement) {
        this.fm_ruleelement = fm_ruleelement;
    }
    public fM_RuleElement getFm_ruleelement() {
        return fm_ruleelement;
    }

    public void setFm_ruleelement(fM_RuleElement fm_ruleelement) {
        this.fm_ruleelement = fm_ruleelement;
    }

}