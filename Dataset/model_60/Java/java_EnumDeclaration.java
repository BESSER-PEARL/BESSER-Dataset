





import java.util.List;
import java.util.ArrayList;

public class java_EnumDeclaration extends AbstractTypeDeclaration {






    private List<java_EnumConstantDeclaration> java_enumconstantdeclarations;


    public java_EnumDeclaration(
    ) {
        super(
        );
        this.java_enumconstantdeclarations = new ArrayList<>();
    }

    public java_EnumDeclaration(
        ArrayList<java_EnumConstantDeclaration> java_enumconstantdeclarations    ) {
        this.java_enumconstantdeclarations = java_enumconstantdeclarations;
    }


    public List<java_EnumConstantDeclaration> getJava_enumconstantdeclarations() {
        return java_enumconstantdeclarations;
    }

    public void addJava_enumconstantdeclaration(Java_enumconstantdeclaration java_enumconstantdeclaration) {
        this.java_enumconstantdeclarations.add(java_enumconstantdeclaration);
    }

}