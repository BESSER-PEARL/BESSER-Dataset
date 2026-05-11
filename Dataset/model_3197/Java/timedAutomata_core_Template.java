





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_Template extends base_Nameable, core_TAElement, base_Identifyable {






    private List<declarations_Declaration> declarations_declarations;


    public timedAutomata_core_Template(
    ) {
        super(
        );
        this.declarations_declarations = new ArrayList<>();
    }

    public timedAutomata_core_Template(
        ArrayList<declarations_Declaration> declarations_declarations    ) {
        this.declarations_declarations = declarations_declarations;
    }


    public List<declarations_Declaration> getDeclarations_declarations() {
        return declarations_declarations;
    }

    public void addDeclarations_declaration(Declarations_declaration declarations_declaration) {
        this.declarations_declarations.add(declarations_declaration);
    }

}