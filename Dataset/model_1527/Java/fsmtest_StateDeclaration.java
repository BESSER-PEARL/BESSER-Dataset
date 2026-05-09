





import java.util.List;
import java.util.ArrayList;

public class fsmtest_StateDeclaration  {

    private String name;





    private List<fsmtest_TransitionDeclaration> fsmtest_transitiondeclarations;




    private fsmtest_TransitionDeclaration fsmtest_transitiondeclaration;




    private List<fsmtest_ConditionDeclaration> fsmtest_conditiondeclarations;




    private fsmtest_FsmDefinition fsmtest_fsmdefinition;


    public fsmtest_StateDeclaration(
        String name    ) {
        this.name = name;
        this.fsmtest_transitiondeclarations = new ArrayList<>();
        this.fsmtest_conditiondeclarations = new ArrayList<>();
    }

    public fsmtest_StateDeclaration(
        String name        ArrayList<fsmtest_TransitionDeclaration> fsmtest_transitiondeclarations,        ArrayList<fsmtest_ConditionDeclaration> fsmtest_conditiondeclarations    ) {
        this.name = name;
        this.fsmtest_transitiondeclarations = fsmtest_transitiondeclarations;
        this.fsmtest_conditiondeclarations = fsmtest_conditiondeclarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fsmtest_TransitionDeclaration> getFsmtest_transitiondeclarations() {
        return fsmtest_transitiondeclarations;
    }

    public void addFsmtest_transitiondeclaration(Fsmtest_transitiondeclaration fsmtest_transitiondeclaration) {
        this.fsmtest_transitiondeclarations.add(fsmtest_transitiondeclaration);
    }
    public fsmtest_TransitionDeclaration getFsmtest_transitiondeclaration() {
        return fsmtest_transitiondeclaration;
    }

    public void setFsmtest_transitiondeclaration(fsmtest_TransitionDeclaration fsmtest_transitiondeclaration) {
        this.fsmtest_transitiondeclaration = fsmtest_transitiondeclaration;
    }
    public List<fsmtest_ConditionDeclaration> getFsmtest_conditiondeclarations() {
        return fsmtest_conditiondeclarations;
    }

    public void addFsmtest_conditiondeclaration(Fsmtest_conditiondeclaration fsmtest_conditiondeclaration) {
        this.fsmtest_conditiondeclarations.add(fsmtest_conditiondeclaration);
    }
    public fsmtest_FsmDefinition getFsmtest_fsmdefinition() {
        return fsmtest_fsmdefinition;
    }

    public void setFsmtest_fsmdefinition(fsmtest_FsmDefinition fsmtest_fsmdefinition) {
        this.fsmtest_fsmdefinition = fsmtest_fsmdefinition;
    }

}