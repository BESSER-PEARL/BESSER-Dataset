





import java.util.List;
import java.util.ArrayList;

public class gore_GoalModel  {

    private String internalId;





    private gore_Goal gore_goal;




    private gore_Configuration gore_configuration;




    private List<gore_DifferentialRelation> gore_differentialrelations;




    private gore_Goal gore_goal;




    private List<gore_Actor> gore_actors;




    private gore_Configuration gore_configuration;




    private gore_Actor gore_actor;


    public gore_GoalModel(
        String internalId    ) {
        this.internalId = internalId;
        this.gore_differentialrelations = new ArrayList<>();
        this.gore_actors = new ArrayList<>();
    }

    public gore_GoalModel(
        String internalId        ArrayList<gore_DifferentialRelation> gore_differentialrelations,        ArrayList<gore_Actor> gore_actors    ) {
        this.internalId = internalId;
        this.gore_differentialrelations = gore_differentialrelations;
        this.gore_actors = gore_actors;
    }

    public String getInternalid() {
        return internalId;
    }

    public void setInternalid(String internalId) {
        this.internalId = internalId;
    }

    public gore_Goal getGore_goal() {
        return gore_goal;
    }

    public void setGore_goal(gore_Goal gore_goal) {
        this.gore_goal = gore_goal;
    }
    public gore_Configuration getGore_configuration() {
        return gore_configuration;
    }

    public void setGore_configuration(gore_Configuration gore_configuration) {
        this.gore_configuration = gore_configuration;
    }
    public List<gore_DifferentialRelation> getGore_differentialrelations() {
        return gore_differentialrelations;
    }

    public void addGore_differentialrelation(Gore_differentialrelation gore_differentialrelation) {
        this.gore_differentialrelations.add(gore_differentialrelation);
    }
    public gore_Goal getGore_goal() {
        return gore_goal;
    }

    public void setGore_goal(gore_Goal gore_goal) {
        this.gore_goal = gore_goal;
    }
    public List<gore_Actor> getGore_actors() {
        return gore_actors;
    }

    public void addGore_actor(Gore_actor gore_actor) {
        this.gore_actors.add(gore_actor);
    }
    public gore_Configuration getGore_configuration() {
        return gore_configuration;
    }

    public void setGore_configuration(gore_Configuration gore_configuration) {
        this.gore_configuration = gore_configuration;
    }
    public gore_Actor getGore_actor() {
        return gore_actor;
    }

    public void setGore_actor(gore_Actor gore_actor) {
        this.gore_actor = gore_actor;
    }

}