





import java.util.List;
import java.util.ArrayList;

public class Ant_Target  {

    private String name;
    private String description;
    private String unless;
    private String ifCondition;





    private List<Target> targets;


    public Ant_Target(
        String name,        String description,        String unless,        String ifCondition    ) {
        this.name = name;
        this.description = description;
        this.unless = unless;
        this.ifCondition = ifCondition;
        this.targets = new ArrayList<>();
    }

    public Ant_Target(
        String name,        String description,        String unless,        String ifCondition        ArrayList<Target> targets    ) {
        this.name = name;
        this.description = description;
        this.unless = unless;
        this.ifCondition = ifCondition;
        this.targets = targets;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getUnless() {
        return unless;
    }

    public void setUnless(String unless) {
        this.unless = unless;
    }
    public String getIfcondition() {
        return ifCondition;
    }

    public void setIfcondition(String ifCondition) {
        this.ifCondition = ifCondition;
    }

    public List<Target> getTargets() {
        return targets;
    }

    public void addTarget(Target target) {
        this.targets.add(target);
    }

}