





import java.util.List;
import java.util.ArrayList;

public class Ant_Target  {

    private String name;
    private String unless;
    private String ifCondition;
    private String description;





    private List<Target> targets;


    public Ant_Target(
        String name,        String unless,        String ifCondition,        String description    ) {
        this.name = name;
        this.unless = unless;
        this.ifCondition = ifCondition;
        this.description = description;
        this.targets = new ArrayList<>();
    }

    public Ant_Target(
        String name,        String unless,        String ifCondition,        String description        ArrayList<Target> targets    ) {
        this.name = name;
        this.unless = unless;
        this.ifCondition = ifCondition;
        this.description = description;
        this.targets = targets;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Target> getTargets() {
        return targets;
    }

    public void addTarget(Target target) {
        this.targets.add(target);
    }

}