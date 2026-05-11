





import java.util.List;
import java.util.ArrayList;

public class TTMCConstraint_ParametricElement  {






    private List<TTMCConstraint_ParameterDeclaration> ttmcconstraint_parameterdeclarations;


    public TTMCConstraint_ParametricElement(
    ) {
        this.ttmcconstraint_parameterdeclarations = new ArrayList<>();
    }

    public TTMCConstraint_ParametricElement(
        ArrayList<TTMCConstraint_ParameterDeclaration> ttmcconstraint_parameterdeclarations    ) {
        this.ttmcconstraint_parameterdeclarations = ttmcconstraint_parameterdeclarations;
    }


    public List<TTMCConstraint_ParameterDeclaration> getTtmcconstraint_parameterdeclarations() {
        return ttmcconstraint_parameterdeclarations;
    }

    public void addTtmcconstraint_parameterdeclaration(Ttmcconstraint_parameterdeclaration ttmcconstraint_parameterdeclaration) {
        this.ttmcconstraint_parameterdeclarations.add(ttmcconstraint_parameterdeclaration);
    }

}