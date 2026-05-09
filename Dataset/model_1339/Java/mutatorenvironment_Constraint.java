





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_Constraint  {

    private None rules;
    private None id;





    private mutatorenvironment_MutatorEnvironment mutatorenvironment_mutatorenvironment;




    private mutatorenvironment_EClass mutatorenvironment_eclass;


    public mutatorenvironment_Constraint(
        None rules,        None id    ) {
        this.rules = rules;
        this.id = id;
    }


    public None getRules() {
        return rules;
    }

    public void setRules(None rules) {
        this.rules = rules;
    }
    public None getId() {
        return id;
    }

    public void setId(None id) {
        this.id = id;
    }

    public mutatorenvironment_MutatorEnvironment getMutatorenvironment_mutatorenvironment() {
        return mutatorenvironment_mutatorenvironment;
    }

    public void setMutatorenvironment_mutatorenvironment(mutatorenvironment_MutatorEnvironment mutatorenvironment_mutatorenvironment) {
        this.mutatorenvironment_mutatorenvironment = mutatorenvironment_mutatorenvironment;
    }
    public mutatorenvironment_EClass getMutatorenvironment_eclass() {
        return mutatorenvironment_eclass;
    }

    public void setMutatorenvironment_eclass(mutatorenvironment_EClass mutatorenvironment_eclass) {
        this.mutatorenvironment_eclass = mutatorenvironment_eclass;
    }

}