





import java.util.List;
import java.util.ArrayList;

public class myAtl_CalledRule extends ModuleElement {






    private myAtl_ActionBlock myatl_actionblock;




    private myAtl_OutPattern myatl_outpattern;




    private List<myAtl_RuleVariableDeclaration> myatl_rulevariabledeclarations;


    public myAtl_CalledRule(
    ) {
        super(
        );
        this.myatl_rulevariabledeclarations = new ArrayList<>();
    }

    public myAtl_CalledRule(
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
    public List<myAtl_RuleVariableDeclaration> getMyatl_rulevariabledeclarations() {
        return myatl_rulevariabledeclarations;
    }

    public void addMyatl_rulevariabledeclaration(Myatl_rulevariabledeclaration myatl_rulevariabledeclaration) {
        this.myatl_rulevariabledeclarations.add(myatl_rulevariabledeclaration);
    }

}