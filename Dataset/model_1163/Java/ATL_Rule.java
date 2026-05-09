





import java.util.List;
import java.util.ArrayList;

public class ATL_Rule extends ModuleElement {

    private String name;





    private ActionBlock actionblock;




    private List<RuleVariableDeclaration> rulevariabledeclarations;


    public ATL_Rule(
        String name    ) {
        super(
        );
        this.name = name;
        this.rulevariabledeclarations = new ArrayList<>();
    }

    public ATL_Rule(
        String name        ArrayList<RuleVariableDeclaration> rulevariabledeclarations    ) {
        this.name = name;
        this.rulevariabledeclarations = rulevariabledeclarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ActionBlock getActionblock() {
        return actionblock;
    }

    public void setActionblock(ActionBlock actionblock) {
        this.actionblock = actionblock;
    }
    public List<RuleVariableDeclaration> getRulevariabledeclarations() {
        return rulevariabledeclarations;
    }

    public void addRulevariabledeclaration(Rulevariabledeclaration rulevariabledeclaration) {
        this.rulevariabledeclarations.add(rulevariabledeclaration);
    }

}