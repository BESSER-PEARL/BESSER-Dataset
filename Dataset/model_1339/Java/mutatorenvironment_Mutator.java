





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_Mutator extends ObjectEmitter {

    private None max;
    private None fixed;
    private None min;





    private mutatorenvironment_MutatorEnvironment mutatorenvironment_mutatorenvironment;


    public mutatorenvironment_Mutator(
        None max,        None fixed,        None min    ) {
        super(
        );
        this.max = max;
        this.fixed = fixed;
        this.min = min;
    }


    public None getMax() {
        return max;
    }

    public void setMax(None max) {
        this.max = max;
    }
    public None getFixed() {
        return fixed;
    }

    public void setFixed(None fixed) {
        this.fixed = fixed;
    }
    public None getMin() {
        return min;
    }

    public void setMin(None min) {
        this.min = min;
    }

    public mutatorenvironment_MutatorEnvironment getMutatorenvironment_mutatorenvironment() {
        return mutatorenvironment_mutatorenvironment;
    }

    public void setMutatorenvironment_mutatorenvironment(mutatorenvironment_MutatorEnvironment mutatorenvironment_mutatorenvironment) {
        this.mutatorenvironment_mutatorenvironment = mutatorenvironment_mutatorenvironment;
    }

}