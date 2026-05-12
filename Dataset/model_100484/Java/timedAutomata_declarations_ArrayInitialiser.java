





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_declarations_ArrayInitialiser extends Initialiser {






    private List<declarations_Initialiser> declarations_initialisers;


    public timedAutomata_declarations_ArrayInitialiser(
    ) {
        super(
        );
        this.declarations_initialisers = new ArrayList<>();
    }

    public timedAutomata_declarations_ArrayInitialiser(
        ArrayList<declarations_Initialiser> declarations_initialisers    ) {
        this.declarations_initialisers = declarations_initialisers;
    }


    public List<declarations_Initialiser> getDeclarations_initialisers() {
        return declarations_initialisers;
    }

    public void addDeclarations_initialiser(Declarations_initialiser declarations_initialiser) {
        this.declarations_initialisers.add(declarations_initialiser);
    }

}