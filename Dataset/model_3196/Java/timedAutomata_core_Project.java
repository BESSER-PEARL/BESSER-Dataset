





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_Project extends TAElement {

    private String id;





    private List<declarations_Declaration> declarations_declarations;


    public timedAutomata_core_Project(
        String id    ) {
        super(
        );
        this.id = id;
        this.declarations_declarations = new ArrayList<>();
    }

    public timedAutomata_core_Project(
        String id        ArrayList<declarations_Declaration> declarations_declarations    ) {
        this.id = id;
        this.declarations_declarations = declarations_declarations;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<declarations_Declaration> getDeclarations_declarations() {
        return declarations_declarations;
    }

    public void addDeclarations_declaration(Declarations_declaration declarations_declaration) {
        this.declarations_declarations.add(declarations_declaration);
    }

}