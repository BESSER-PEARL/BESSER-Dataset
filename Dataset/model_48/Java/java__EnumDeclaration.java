





import java.util.List;
import java.util.ArrayList;

public class java__EnumDeclaration extends AbstractTypeDeclaration {






    private List<java__EnumConstantDeclaration> java__enumconstantdeclarations;


    public java__EnumDeclaration(
    ) {
        super(
        );
        this.java__enumconstantdeclarations = new ArrayList<>();
    }

    public java__EnumDeclaration(
        ArrayList<java__EnumConstantDeclaration> java__enumconstantdeclarations    ) {
        this.java__enumconstantdeclarations = java__enumconstantdeclarations;
    }


    public List<java__EnumConstantDeclaration> getJava__enumconstantdeclarations() {
        return java__enumconstantdeclarations;
    }

    public void addJava__enumconstantdeclaration(Java__enumconstantdeclaration java__enumconstantdeclaration) {
        this.java__enumconstantdeclarations.add(java__enumconstantdeclaration);
    }

}