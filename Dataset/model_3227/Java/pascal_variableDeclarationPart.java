





import java.util.List;
import java.util.ArrayList;

public class pascal_variableDeclarationPart  {






    private List<pascal_variableDeclaration> pascal_variabledeclarations;




    private pascal_block pascal_block;




    private pascal_variableDeclaration pascal_variabledeclaration;


    public pascal_variableDeclarationPart(
    ) {
        this.pascal_variabledeclarations = new ArrayList<>();
    }

    public pascal_variableDeclarationPart(
        ArrayList<pascal_variableDeclaration> pascal_variabledeclarations    ) {
        this.pascal_variabledeclarations = pascal_variabledeclarations;
    }


    public List<pascal_variableDeclaration> getPascal_variabledeclarations() {
        return pascal_variabledeclarations;
    }

    public void addPascal_variabledeclaration(Pascal_variabledeclaration pascal_variabledeclaration) {
        this.pascal_variabledeclarations.add(pascal_variabledeclaration);
    }
    public pascal_block getPascal_block() {
        return pascal_block;
    }

    public void setPascal_block(pascal_block pascal_block) {
        this.pascal_block = pascal_block;
    }
    public pascal_variableDeclaration getPascal_variabledeclaration() {
        return pascal_variabledeclaration;
    }

    public void setPascal_variabledeclaration(pascal_variableDeclaration pascal_variabledeclaration) {
        this.pascal_variabledeclaration = pascal_variabledeclaration;
    }

}