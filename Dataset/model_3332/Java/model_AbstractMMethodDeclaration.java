





import java.util.List;
import java.util.ArrayList;

public class model_AbstractMMethodDeclaration extends AbstractMTypeWithNameDeclaration {






    private List<model_MMethodDeclarationParameter> model_mmethoddeclarationparameters;




    private model_MMethodDeclarationParameter model_mmethoddeclarationparameter;


    public model_AbstractMMethodDeclaration(
    ) {
        super(
        );
        this.model_mmethoddeclarationparameters = new ArrayList<>();
    }

    public model_AbstractMMethodDeclaration(
        ArrayList<model_MMethodDeclarationParameter> model_mmethoddeclarationparameters    ) {
        this.model_mmethoddeclarationparameters = model_mmethoddeclarationparameters;
    }


    public List<model_MMethodDeclarationParameter> getModel_mmethoddeclarationparameters() {
        return model_mmethoddeclarationparameters;
    }

    public void addModel_mmethoddeclarationparameter(Model_mmethoddeclarationparameter model_mmethoddeclarationparameter) {
        this.model_mmethoddeclarationparameters.add(model_mmethoddeclarationparameter);
    }
    public model_MMethodDeclarationParameter getModel_mmethoddeclarationparameter() {
        return model_mmethoddeclarationparameter;
    }

    public void setModel_mmethoddeclarationparameter(model_MMethodDeclarationParameter model_mmethoddeclarationparameter) {
        this.model_mmethoddeclarationparameter = model_mmethoddeclarationparameter;
    }

}