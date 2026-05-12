





import java.util.List;
import java.util.ArrayList;

public class requirements_Goal extends AnnotableElement {

    private String priority;
    private String synopsis;





    private List<requirements_PrivilegeGroup> requirements_privilegegroups;




    private List<requirements_Goal> requirements_goals;


    public requirements_Goal(
        String priority,        String synopsis    ) {
        super(
        );
        this.priority = priority;
        this.synopsis = synopsis;
        this.requirements_privilegegroups = new ArrayList<>();
        this.requirements_goals = new ArrayList<>();
    }

    public requirements_Goal(
        String priority,        String synopsis        ArrayList<requirements_PrivilegeGroup> requirements_privilegegroups,        ArrayList<requirements_Goal> requirements_goals    ) {
        this.priority = priority;
        this.synopsis = synopsis;
        this.requirements_privilegegroups = requirements_privilegegroups;
        this.requirements_goals = requirements_goals;
    }

    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getSynopsis() {
        return synopsis;
    }

    public void setSynopsis(String synopsis) {
        this.synopsis = synopsis;
    }

    public List<requirements_PrivilegeGroup> getRequirements_privilegegroups() {
        return requirements_privilegegroups;
    }

    public void addRequirements_privilegegroup(Requirements_privilegegroup requirements_privilegegroup) {
        this.requirements_privilegegroups.add(requirements_privilegegroup);
    }
    public List<requirements_Goal> getRequirements_goals() {
        return requirements_goals;
    }

    public void addRequirements_goal(Requirements_goal requirements_goal) {
        this.requirements_goals.add(requirements_goal);
    }

}