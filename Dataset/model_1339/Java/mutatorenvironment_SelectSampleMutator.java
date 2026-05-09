





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_SelectSampleMutator extends Mutator {

    private None clause;





    private mutatorenvironment_ObSelectionStrategy mutatorenvironment_obselectionstrategy;


    public mutatorenvironment_SelectSampleMutator(
        None clause    ) {
        super(
        );
        this.clause = clause;
    }


    public None getClause() {
        return clause;
    }

    public void setClause(None clause) {
        this.clause = clause;
    }

    public mutatorenvironment_ObSelectionStrategy getMutatorenvironment_obselectionstrategy() {
        return mutatorenvironment_obselectionstrategy;
    }

    public void setMutatorenvironment_obselectionstrategy(mutatorenvironment_ObSelectionStrategy mutatorenvironment_obselectionstrategy) {
        this.mutatorenvironment_obselectionstrategy = mutatorenvironment_obselectionstrategy;
    }

}