





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_Block  {

    private None fixed;
    private None min;
    private None description;
    private None repeat;
    private None name;
    private None max;





    private mutatorenvironment_MutatorEnvironment mutatorenvironment_mutatorenvironment;




    private List<mutatorenvironment_Mutator> mutatorenvironment_mutators;




    private List<mutatorenvironment_Block> mutatorenvironment_blocks;


    public mutatorenvironment_Block(
        None fixed,        None min,        None description,        None repeat,        None name,        None max    ) {
        this.fixed = fixed;
        this.min = min;
        this.description = description;
        this.repeat = repeat;
        this.name = name;
        this.max = max;
        this.mutatorenvironment_mutators = new ArrayList<>();
        this.mutatorenvironment_blocks = new ArrayList<>();
    }

    public mutatorenvironment_Block(
        None fixed,        None min,        None description,        None repeat,        None name,        None max        ArrayList<mutatorenvironment_Mutator> mutatorenvironment_mutators,        ArrayList<mutatorenvironment_Block> mutatorenvironment_blocks    ) {
        this.fixed = fixed;
        this.min = min;
        this.description = description;
        this.repeat = repeat;
        this.name = name;
        this.max = max;
        this.mutatorenvironment_mutators = mutatorenvironment_mutators;
        this.mutatorenvironment_blocks = mutatorenvironment_blocks;
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
    public None getDescription() {
        return description;
    }

    public void setDescription(None description) {
        this.description = description;
    }
    public None getRepeat() {
        return repeat;
    }

    public void setRepeat(None repeat) {
        this.repeat = repeat;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }
    public None getMax() {
        return max;
    }

    public void setMax(None max) {
        this.max = max;
    }

    public mutatorenvironment_MutatorEnvironment getMutatorenvironment_mutatorenvironment() {
        return mutatorenvironment_mutatorenvironment;
    }

    public void setMutatorenvironment_mutatorenvironment(mutatorenvironment_MutatorEnvironment mutatorenvironment_mutatorenvironment) {
        this.mutatorenvironment_mutatorenvironment = mutatorenvironment_mutatorenvironment;
    }
    public List<mutatorenvironment_Mutator> getMutatorenvironment_mutators() {
        return mutatorenvironment_mutators;
    }

    public void addMutatorenvironment_mutator(Mutatorenvironment_mutator mutatorenvironment_mutator) {
        this.mutatorenvironment_mutators.add(mutatorenvironment_mutator);
    }
    public List<mutatorenvironment_Block> getMutatorenvironment_blocks() {
        return mutatorenvironment_blocks;
    }

    public void addMutatorenvironment_block(Mutatorenvironment_block mutatorenvironment_block) {
        this.mutatorenvironment_blocks.add(mutatorenvironment_block);
    }

}