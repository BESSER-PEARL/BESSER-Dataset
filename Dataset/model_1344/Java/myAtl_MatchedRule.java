





import java.util.List;
import java.util.ArrayList;

public class myAtl_MatchedRule extends ModuleElement {






    private myAtl_ActionBlock myatl_actionblock;




    private myAtl_OutPattern myatl_outpattern;




    private myAtl_InPattern myatl_inpattern;




    private List<myAtl_RuleVariableDeclaration> myatl_rulevariabledeclarations;


    public myAtl_MatchedRule(
    ) {
        super(
        );
        this.myatl_rulevariabledeclarations = new ArrayList<>();
    }

    public myAtl_MatchedRule(
        ArrayList<myAtl_RuleVariableDeclaration> myatl_rulevariabledeclarations    ) {
        this.myatl_rulevariabledeclarations = myatl_rulevariabledeclarations;
    }


    public myAtl_ActionBlock getMyatl_actionblock() {
        return myatl_actionblock;
    }

    public void setMyatl_actionblock(myAtl_ActionBlock myatl_actionblock) {
        this.myatl_actionblock = myatl_actionblock;
    }
    public myAtl_OutPattern getMyatl_outpattern() {
        return myatl_outpattern;
    }

    public void setMyatl_outpattern(myAtl_OutPattern myatl_outpattern) {
        this.myatl_outpattern = myatl_outpattern;
    }
    public myAtl_InPattern getMyatl_inpattern() {
        return myatl_inpattern;
    }

    public void setMyatl_inpattern(myAtl_InPattern myatl_inpattern) {
        this.myatl_inpattern = myatl_inpattern;
    }
    public List<myAtl_RuleVariableDeclaration> getMyatl_rulevariabledeclarations() {
        return myatl_rulevariabledeclarations;
    }

    public void addMyatl_rulevariabledeclaration(Myatl_rulevariabledeclaration myatl_rulevariabledeclaration) {
        this.myatl_rulevariabledeclarations.add(myatl_rulevariabledeclaration);
    }

}