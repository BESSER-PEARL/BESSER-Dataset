





import java.util.List;
import java.util.ArrayList;

public class DOM_CompilationUnit extends ASTNode {






    private List<AbstractTypeDeclaration> abstracttypedeclarations;




    private List<ImportDeclaration> importdeclarations;


    public DOM_CompilationUnit(
    ) {
        super(
        );
        this.abstracttypedeclarations = new ArrayList<>();
        this.importdeclarations = new ArrayList<>();
    }

    public DOM_CompilationUnit(
        ArrayList<AbstractTypeDeclaration> abstracttypedeclarations,        ArrayList<ImportDeclaration> importdeclarations    ) {
        this.abstracttypedeclarations = abstracttypedeclarations;
        this.importdeclarations = importdeclarations;
    }


    public List<AbstractTypeDeclaration> getAbstracttypedeclarations() {
        return abstracttypedeclarations;
    }

    public void addAbstracttypedeclaration(Abstracttypedeclaration abstracttypedeclaration) {
        this.abstracttypedeclarations.add(abstracttypedeclaration);
    }
    public List<ImportDeclaration> getImportdeclarations() {
        return importdeclarations;
    }

    public void addImportdeclaration(Importdeclaration importdeclaration) {
        this.importdeclarations.add(importdeclaration);
    }

}