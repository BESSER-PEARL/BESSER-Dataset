





import java.util.List;
import java.util.ArrayList;

public class NBVR_Logic_Argument  {






    private Variable variable;




    private Relation relation;




    private RolePhrase rolephrase;




    private VerbRole verbrole;




    private Argument argument;


    public NBVR_Logic_Argument(
    ) {
    }



    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public Relation getRelation() {
        return relation;
    }

    public void setRelation(Relation relation) {
        this.relation = relation;
    }
    public RolePhrase getRolephrase() {
        return rolephrase;
    }

    public void setRolephrase(RolePhrase rolephrase) {
        this.rolephrase = rolephrase;
    }
    public VerbRole getVerbrole() {
        return verbrole;
    }

    public void setVerbrole(VerbRole verbrole) {
        this.verbrole = verbrole;
    }
    public Argument getArgument() {
        return argument;
    }

    public void setArgument(Argument argument) {
        this.argument = argument;
    }

}