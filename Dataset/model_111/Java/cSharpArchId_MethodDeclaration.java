





import java.util.List;
import java.util.ArrayList;

public class cSharpArchId_MethodDeclaration extends AbstractMethodDeclaration {






    private List<cSharpArchId_BodyDeclaration> csharparchid_bodydeclarations;


    public cSharpArchId_MethodDeclaration(
    ) {
        super(
        );
        this.csharparchid_bodydeclarations = new ArrayList<>();
    }

    public cSharpArchId_MethodDeclaration(
        ArrayList<cSharpArchId_BodyDeclaration> csharparchid_bodydeclarations    ) {
        this.csharparchid_bodydeclarations = csharparchid_bodydeclarations;
    }


    public List<cSharpArchId_BodyDeclaration> getCsharparchid_bodydeclarations() {
        return csharparchid_bodydeclarations;
    }

    public void addCsharparchid_bodydeclaration(Csharparchid_bodydeclaration csharparchid_bodydeclaration) {
        this.csharparchid_bodydeclarations.add(csharparchid_bodydeclaration);
    }

}