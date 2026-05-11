





import java.util.List;
import java.util.ArrayList;

public class camel_scalability_ScalabilityRule  {

    private String name;





    private Event event;




    private List<ScaleRequirement> scalerequirements;




    private List<Entity> entitys;




    private List<scalability_camel_Action> scalability_camel_actions;


    public camel_scalability_ScalabilityRule(
        String name    ) {
        this.name = name;
        this.scalerequirements = new ArrayList<>();
        this.entitys = new ArrayList<>();
        this.scalability_camel_actions = new ArrayList<>();
    }

    public camel_scalability_ScalabilityRule(
        String name        ArrayList<ScaleRequirement> scalerequirements,        ArrayList<Entity> entitys,        ArrayList<scalability_camel_Action> scalability_camel_actions    ) {
        this.name = name;
        this.scalerequirements = scalerequirements;
        this.entitys = entitys;
        this.scalability_camel_actions = scalability_camel_actions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Event getEvent() {
        return event;
    }

    public void setEvent(Event event) {
        this.event = event;
    }
    public List<ScaleRequirement> getScalerequirements() {
        return scalerequirements;
    }

    public void addScalerequirement(Scalerequirement scalerequirement) {
        this.scalerequirements.add(scalerequirement);
    }
    public List<Entity> getEntitys() {
        return entitys;
    }

    public void addEntity(Entity entity) {
        this.entitys.add(entity);
    }
    public List<scalability_camel_Action> getScalability_camel_actions() {
        return scalability_camel_actions;
    }

    public void addScalability_camel_action(Scalability_camel_action scalability_camel_action) {
        this.scalability_camel_actions.add(scalability_camel_action);
    }

}