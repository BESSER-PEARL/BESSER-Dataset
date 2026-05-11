





import java.util.List;
import java.util.ArrayList;

public class dbl_RuleExpr extends RhsExpression {






    private dbl_ExtensionRule dbl_extensionrule;




    private dbl_TsRule dbl_tsrule;


    public dbl_RuleExpr(
    ) {
        super(
        );
    }



    public dbl_ExtensionRule getDbl_extensionrule() {
        return dbl_extensionrule;
    }

    public void setDbl_extensionrule(dbl_ExtensionRule dbl_extensionrule) {
        this.dbl_extensionrule = dbl_extensionrule;
    }
    public dbl_TsRule getDbl_tsrule() {
        return dbl_tsrule;
    }

    public void setDbl_tsrule(dbl_TsRule dbl_tsrule) {
        this.dbl_tsrule = dbl_tsrule;
    }

}