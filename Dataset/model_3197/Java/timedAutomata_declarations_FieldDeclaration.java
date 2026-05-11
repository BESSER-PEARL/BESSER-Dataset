





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_declarations_FieldDeclaration  {






    private List<declarations_ArrayDeclaration> declarations_arraydeclarations;




    private types_Type types_type;


    public timedAutomata_declarations_FieldDeclaration(
    ) {
        this.declarations_arraydeclarations = new ArrayList<>();
    }

    public timedAutomata_declarations_FieldDeclaration(
        ArrayList<declarations_ArrayDeclaration> declarations_arraydeclarations    ) {
        this.declarations_arraydeclarations = declarations_arraydeclarations;
    }


    public List<declarations_ArrayDeclaration> getDeclarations_arraydeclarations() {
        return declarations_arraydeclarations;
    }

    public void addDeclarations_arraydeclaration(Declarations_arraydeclaration declarations_arraydeclaration) {
        this.declarations_arraydeclarations.add(declarations_arraydeclaration);
    }
    public types_Type getTypes_type() {
        return types_type;
    }

    public void setTypes_type(types_Type types_type) {
        this.types_type = types_type;
    }

}