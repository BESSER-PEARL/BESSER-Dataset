





import java.util.List;
import java.util.ArrayList;

public class TTMCConstraint_ConstraintSpecification extends ParametricElement, NamedElement {






    private List<TTMCConstraint_BasicConstraintDefinition> ttmcconstraint_basicconstraintdefinitions;




    private List<TTMCConstraint_ConstantDeclaration> ttmcconstraint_constantdeclarations;




    private List<TTMCConstraint_FunctionDeclaration> ttmcconstraint_functiondeclarations;


    public TTMCConstraint_ConstraintSpecification(
    ) {
        super(
        );
        this.ttmcconstraint_basicconstraintdefinitions = new ArrayList<>();
        this.ttmcconstraint_constantdeclarations = new ArrayList<>();
        this.ttmcconstraint_functiondeclarations = new ArrayList<>();
    }

    public TTMCConstraint_ConstraintSpecification(
        ArrayList<TTMCConstraint_BasicConstraintDefinition> ttmcconstraint_basicconstraintdefinitions,        ArrayList<TTMCConstraint_ConstantDeclaration> ttmcconstraint_constantdeclarations,        ArrayList<TTMCConstraint_FunctionDeclaration> ttmcconstraint_functiondeclarations    ) {
        this.ttmcconstraint_basicconstraintdefinitions = ttmcconstraint_basicconstraintdefinitions;
        this.ttmcconstraint_constantdeclarations = ttmcconstraint_constantdeclarations;
        this.ttmcconstraint_functiondeclarations = ttmcconstraint_functiondeclarations;
    }


    public List<TTMCConstraint_BasicConstraintDefinition> getTtmcconstraint_basicconstraintdefinitions() {
        return ttmcconstraint_basicconstraintdefinitions;
    }

    public void addTtmcconstraint_basicconstraintdefinition(Ttmcconstraint_basicconstraintdefinition ttmcconstraint_basicconstraintdefinition) {
        this.ttmcconstraint_basicconstraintdefinitions.add(ttmcconstraint_basicconstraintdefinition);
    }
    public List<TTMCConstraint_ConstantDeclaration> getTtmcconstraint_constantdeclarations() {
        return ttmcconstraint_constantdeclarations;
    }

    public void addTtmcconstraint_constantdeclaration(Ttmcconstraint_constantdeclaration ttmcconstraint_constantdeclaration) {
        this.ttmcconstraint_constantdeclarations.add(ttmcconstraint_constantdeclaration);
    }
    public List<TTMCConstraint_FunctionDeclaration> getTtmcconstraint_functiondeclarations() {
        return ttmcconstraint_functiondeclarations;
    }

    public void addTtmcconstraint_functiondeclaration(Ttmcconstraint_functiondeclaration ttmcconstraint_functiondeclaration) {
        this.ttmcconstraint_functiondeclarations.add(ttmcconstraint_functiondeclaration);
    }

}