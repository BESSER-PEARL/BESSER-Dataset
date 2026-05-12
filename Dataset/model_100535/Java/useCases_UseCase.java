





import java.util.List;
import java.util.ArrayList;

public class useCases_UseCase  {

    private String goals;
    private String ucName;
    private String name;





    private List<useCases_Actor> usecases_actors;




    private useCases_PackageDeclaration usecases_packagedeclaration;




    private List<useCases_RequirementRef> usecases_requirementrefs;


    public useCases_UseCase(
        String goals,        String ucName,        String name    ) {
        this.goals = goals;
        this.ucName = ucName;
        this.name = name;
        this.usecases_actors = new ArrayList<>();
        this.usecases_requirementrefs = new ArrayList<>();
    }

    public useCases_UseCase(
        String goals,        String ucName,        String name        ArrayList<useCases_Actor> usecases_actors,        ArrayList<useCases_RequirementRef> usecases_requirementrefs    ) {
        this.goals = goals;
        this.ucName = ucName;
        this.name = name;
        this.usecases_actors = usecases_actors;
        this.usecases_requirementrefs = usecases_requirementrefs;
    }

    public String getGoals() {
        return goals;
    }

    public void setGoals(String goals) {
        this.goals = goals;
    }
    public String getUcname() {
        return ucName;
    }

    public void setUcname(String ucName) {
        this.ucName = ucName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<useCases_Actor> getUsecases_actors() {
        return usecases_actors;
    }

    public void addUsecases_actor(Usecases_actor usecases_actor) {
        this.usecases_actors.add(usecases_actor);
    }
    public useCases_PackageDeclaration getUsecases_packagedeclaration() {
        return usecases_packagedeclaration;
    }

    public void setUsecases_packagedeclaration(useCases_PackageDeclaration usecases_packagedeclaration) {
        this.usecases_packagedeclaration = usecases_packagedeclaration;
    }
    public List<useCases_RequirementRef> getUsecases_requirementrefs() {
        return usecases_requirementrefs;
    }

    public void addUsecases_requirementref(Usecases_requirementref usecases_requirementref) {
        this.usecases_requirementrefs.add(usecases_requirementref);
    }

}