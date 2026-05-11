





import java.util.List;
import java.util.ArrayList;

public class model_ExpressionPackage extends ParametricElement, NamedElement {






    private List<model_BasicConstraintDefinition> model_basicconstraintdefinitions;




    private List<model_ConstantDeclaration> model_constantdeclarations;




    private List<model_FunctionDeclaration> model_functiondeclarations;




    private List<model_TypeDeclaration> model_typedeclarations;


    public model_ExpressionPackage(
    ) {
        super(
        );
        this.model_basicconstraintdefinitions = new ArrayList<>();
        this.model_constantdeclarations = new ArrayList<>();
        this.model_functiondeclarations = new ArrayList<>();
        this.model_typedeclarations = new ArrayList<>();
    }

    public model_ExpressionPackage(
        ArrayList<model_BasicConstraintDefinition> model_basicconstraintdefinitions,        ArrayList<model_ConstantDeclaration> model_constantdeclarations,        ArrayList<model_FunctionDeclaration> model_functiondeclarations,        ArrayList<model_TypeDeclaration> model_typedeclarations    ) {
        this.model_basicconstraintdefinitions = model_basicconstraintdefinitions;
        this.model_constantdeclarations = model_constantdeclarations;
        this.model_functiondeclarations = model_functiondeclarations;
        this.model_typedeclarations = model_typedeclarations;
    }


    public List<model_BasicConstraintDefinition> getModel_basicconstraintdefinitions() {
        return model_basicconstraintdefinitions;
    }

    public void addModel_basicconstraintdefinition(Model_basicconstraintdefinition model_basicconstraintdefinition) {
        this.model_basicconstraintdefinitions.add(model_basicconstraintdefinition);
    }
    public List<model_ConstantDeclaration> getModel_constantdeclarations() {
        return model_constantdeclarations;
    }

    public void addModel_constantdeclaration(Model_constantdeclaration model_constantdeclaration) {
        this.model_constantdeclarations.add(model_constantdeclaration);
    }
    public List<model_FunctionDeclaration> getModel_functiondeclarations() {
        return model_functiondeclarations;
    }

    public void addModel_functiondeclaration(Model_functiondeclaration model_functiondeclaration) {
        this.model_functiondeclarations.add(model_functiondeclaration);
    }
    public List<model_TypeDeclaration> getModel_typedeclarations() {
        return model_typedeclarations;
    }

    public void addModel_typedeclaration(Model_typedeclaration model_typedeclaration) {
        this.model_typedeclarations.add(model_typedeclaration);
    }

}