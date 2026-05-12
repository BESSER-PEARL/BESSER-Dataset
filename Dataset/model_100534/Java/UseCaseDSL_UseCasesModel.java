





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_UseCasesModel  {






    private List<UseCaseDSL_PackageDeclaration> usecasedsl_packagedeclarations;


    public UseCaseDSL_UseCasesModel(
    ) {
        this.usecasedsl_packagedeclarations = new ArrayList<>();
    }

    public UseCaseDSL_UseCasesModel(
        ArrayList<UseCaseDSL_PackageDeclaration> usecasedsl_packagedeclarations    ) {
        this.usecasedsl_packagedeclarations = usecasedsl_packagedeclarations;
    }


    public List<UseCaseDSL_PackageDeclaration> getUsecasedsl_packagedeclarations() {
        return usecasedsl_packagedeclarations;
    }

    public void addUsecasedsl_packagedeclaration(Usecasedsl_packagedeclaration usecasedsl_packagedeclaration) {
        this.usecasedsl_packagedeclarations.add(usecasedsl_packagedeclaration);
    }

}