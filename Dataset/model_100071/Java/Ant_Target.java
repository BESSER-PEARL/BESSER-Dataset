





import java.util.List;
import java.util.ArrayList;

public class Ant_Target  {

    private String ifCondition;
    private String description;
    private String name;
    private String unless;





    private List<Ant_Target> ant_targets;




    private Ant_Project ant_project;




    private Ant_Project ant_project;


    public Ant_Target(
        String ifCondition,        String description,        String name,        String unless    ) {
        this.ifCondition = ifCondition;
        this.description = description;
        this.name = name;
        this.unless = unless;
        this.ant_targets = new ArrayList<>();
    }

    public Ant_Target(
        String ifCondition,        String description,        String name,        String unless        ArrayList<Ant_Target> ant_targets    ) {
        this.ifCondition = ifCondition;
        this.description = description;
        this.name = name;
        this.unless = unless;
        this.ant_targets = ant_targets;
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

    public List<Ant_Target> getAnt_targets() {
        return ant_targets;
    }

    public void addAnt_target(Ant_target ant_target) {
        this.ant_targets.add(ant_target);
    }
    public Ant_Project getAnt_project() {
        return ant_project;
    }

    public void setAnt_project(Ant_Project ant_project) {
        this.ant_project = ant_project;
    }
    public Ant_Project getAnt_project() {
        return ant_project;
    }

    public void setAnt_project(Ant_Project ant_project) {
        this.ant_project = ant_project;
    }

}