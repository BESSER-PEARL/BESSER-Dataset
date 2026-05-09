





import java.util.List;
import java.util.ArrayList;

public class Rule  {






    private ATL_RuleVariableDeclaration atl_rulevariabledeclaration;




    private ATL_ActionBlock atl_actionblock;




    private ATL_OutPattern atl_outpattern;


    public Rule(
    ) {
    }



    public ATL_RuleVariableDeclaration getAtl_rulevariabledeclaration() {
        return atl_rulevariabledeclaration;
    }

    public void setAtl_rulevariabledeclaration(ATL_RuleVariableDeclaration atl_rulevariabledeclaration) {
        this.atl_rulevariabledeclaration = atl_rulevariabledeclaration;
    }
    public ATL_ActionBlock getAtl_actionblock() {
        return atl_actionblock;
    }

    public void setAtl_actionblock(ATL_ActionBlock atl_actionblock) {
        this.atl_actionblock = atl_actionblock;
    }
    public ATL_OutPattern getAtl_outpattern() {
        return atl_outpattern;
    }

    public void setAtl_outpattern(ATL_OutPattern atl_outpattern) {
        this.atl_outpattern = atl_outpattern;
    }

}