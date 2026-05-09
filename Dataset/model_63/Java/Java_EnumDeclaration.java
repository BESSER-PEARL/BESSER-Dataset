





import java.util.List;
import java.util.ArrayList;

public class Java_EnumDeclaration extends AbstractTypeDeclaration {






    private List<Java_EnumConstantDeclaration> java_enumconstantdeclarations;


    public Java_EnumDeclaration(
    ) {
        super(
        );
        this.java_enumconstantdeclarations = new ArrayList<>();
    }

    public Java_EnumDeclaration(
        ArrayList<Java_EnumConstantDeclaration> java_enumconstantdeclarations    ) {
        this.java_enumconstantdeclarations = java_enumconstantdeclarations;
    }


    public List<Java_EnumConstantDeclaration> getJava_enumconstantdeclarations() {
        return java_enumconstantdeclarations;
    }

    public void addJava_enumconstantdeclaration(Java_enumconstantdeclaration java_enumconstantdeclaration) {
        this.java_enumconstantdeclarations.add(java_enumconstantdeclaration);
    }

}