





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_CompositeMutator extends Mutator {






    private List<mutatorenvironment_Mutator> mutatorenvironment_mutators;


    public mutatorenvironment_CompositeMutator(
    ) {
        super(
        );
        this.mutatorenvironment_mutators = new ArrayList<>();
    }

    public mutatorenvironment_CompositeMutator(
        ArrayList<mutatorenvironment_Mutator> mutatorenvironment_mutators    ) {
        this.mutatorenvironment_mutators = mutatorenvironment_mutators;
    }


    public List<mutatorenvironment_Mutator> getMutatorenvironment_mutators() {
        return mutatorenvironment_mutators;
    }

    public void addMutatorenvironment_mutator(Mutatorenvironment_mutator mutatorenvironment_mutator) {
        this.mutatorenvironment_mutators.add(mutatorenvironment_mutator);
    }

}