





import java.util.List;
import java.util.ArrayList;

public class AsmL_UpdateFieldRule extends UpdateRule {






    private List<VarTerm> varterms;


    public AsmL_UpdateFieldRule(
    ) {
        super(
        );
        this.varterms = new ArrayList<>();
    }

    public AsmL_UpdateFieldRule(
        ArrayList<VarTerm> varterms    ) {
        this.varterms = varterms;
    }


    public List<VarTerm> getVarterms() {
        return varterms;
    }

    public void addVarterm(Varterm varterm) {
        this.varterms.add(varterm);
    }

}