





import java.util.List;
import java.util.ArrayList;

public class C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration  {






    private List<Declarations_Declaration> declarations_declarations;


    public C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration(
    ) {
        this.declarations_declarations = new ArrayList<>();
    }

    public C_CompilationDirectiveDeclarations_CompilationDirectiveDeclaration(
        ArrayList<Declarations_Declaration> declarations_declarations    ) {
        this.declarations_declarations = declarations_declarations;
    }


    public List<Declarations_Declaration> getDeclarations_declarations() {
        return declarations_declarations;
    }

    public void addDeclarations_declaration(Declarations_declaration declarations_declaration) {
        this.declarations_declarations.add(declarations_declaration);
    }

}