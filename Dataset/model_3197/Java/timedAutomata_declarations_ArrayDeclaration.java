





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_declarations_ArrayDeclaration  {






    private Identifier identifier;




    private List<declarations_ArrayDeclarationType> declarations_arraydeclarationtypes;


    public timedAutomata_declarations_ArrayDeclaration(
    ) {
        this.declarations_arraydeclarationtypes = new ArrayList<>();
    }

    public timedAutomata_declarations_ArrayDeclaration(
        ArrayList<declarations_ArrayDeclarationType> declarations_arraydeclarationtypes    ) {
        this.declarations_arraydeclarationtypes = declarations_arraydeclarationtypes;
    }


    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }
    public List<declarations_ArrayDeclarationType> getDeclarations_arraydeclarationtypes() {
        return declarations_arraydeclarationtypes;
    }

    public void addDeclarations_arraydeclarationtype(Declarations_arraydeclarationtype declarations_arraydeclarationtype) {
        this.declarations_arraydeclarationtypes.add(declarations_arraydeclarationtype);
    }

}