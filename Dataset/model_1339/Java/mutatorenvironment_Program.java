





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_Program extends Definition {

    private None description;
    private None exhaustive;
    private None num;
    private None output;





    private List<mutatorenvironment_Resource> mutatorenvironment_resources;


    public mutatorenvironment_Program(
        None description,        None exhaustive,        None num,        None output    ) {
        super(
        );
        this.description = description;
        this.exhaustive = exhaustive;
        this.num = num;
        this.output = output;
        this.mutatorenvironment_resources = new ArrayList<>();
    }

    public mutatorenvironment_Program(
        None description,        None exhaustive,        None num,        None output        ArrayList<mutatorenvironment_Resource> mutatorenvironment_resources    ) {
        this.description = description;
        this.exhaustive = exhaustive;
        this.num = num;
        this.output = output;
        this.mutatorenvironment_resources = mutatorenvironment_resources;
    }

    public None getDescription() {
        return description;
    }

    public void setDescription(None description) {
        this.description = description;
    }
    public None getExhaustive() {
        return exhaustive;
    }

    public void setExhaustive(None exhaustive) {
        this.exhaustive = exhaustive;
    }
    public None getNum() {
        return num;
    }

    public void setNum(None num) {
        this.num = num;
    }
    public None getOutput() {
        return output;
    }

    public void setOutput(None output) {
        this.output = output;
    }

    public List<mutatorenvironment_Resource> getMutatorenvironment_resources() {
        return mutatorenvironment_resources;
    }

    public void addMutatorenvironment_resource(Mutatorenvironment_resource mutatorenvironment_resource) {
        this.mutatorenvironment_resources.add(mutatorenvironment_resource);
    }

}