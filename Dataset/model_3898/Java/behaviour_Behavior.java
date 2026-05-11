





import java.util.List;
import java.util.ArrayList;

public class behaviour_Behavior  {

    private String behaviorName;
    private String frequency;





    private behaviour_Duration behaviour_duration;




    private List<behaviour_ParameterClass> behaviour_parameterclasss;




    private behaviour_EntityClass behaviour_entityclass;




    private behaviour_Duration behaviour_duration;


    public behaviour_Behavior(
        String behaviorName,        String frequency    ) {
        this.behaviorName = behaviorName;
        this.frequency = frequency;
        this.behaviour_parameterclasss = new ArrayList<>();
    }

    public behaviour_Behavior(
        String behaviorName,        String frequency        ArrayList<behaviour_ParameterClass> behaviour_parameterclasss    ) {
        this.behaviorName = behaviorName;
        this.frequency = frequency;
        this.behaviour_parameterclasss = behaviour_parameterclasss;
    }

    public String getBehaviorname() {
        return behaviorName;
    }

    public void setBehaviorname(String behaviorName) {
        this.behaviorName = behaviorName;
    }
    public String getFrequency() {
        return frequency;
    }

    public void setFrequency(String frequency) {
        this.frequency = frequency;
    }

    public behaviour_Duration getBehaviour_duration() {
        return behaviour_duration;
    }

    public void setBehaviour_duration(behaviour_Duration behaviour_duration) {
        this.behaviour_duration = behaviour_duration;
    }
    public List<behaviour_ParameterClass> getBehaviour_parameterclasss() {
        return behaviour_parameterclasss;
    }

    public void addBehaviour_parameterclass(Behaviour_parameterclass behaviour_parameterclass) {
        this.behaviour_parameterclasss.add(behaviour_parameterclass);
    }
    public behaviour_EntityClass getBehaviour_entityclass() {
        return behaviour_entityclass;
    }

    public void setBehaviour_entityclass(behaviour_EntityClass behaviour_entityclass) {
        this.behaviour_entityclass = behaviour_entityclass;
    }
    public behaviour_Duration getBehaviour_duration() {
        return behaviour_duration;
    }

    public void setBehaviour_duration(behaviour_Duration behaviour_duration) {
        this.behaviour_duration = behaviour_duration;
    }

}