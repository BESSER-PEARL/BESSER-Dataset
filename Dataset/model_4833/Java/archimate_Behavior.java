





import java.util.List;
import java.util.ArrayList;

public class archimate_Behavior  {






    private List<archimate_Behavior> archimate_behaviors;




    private List<archimate_Passive> archimate_passives;




    private archimate_Passive archimate_passive;




    private archimate_Behavior archimate_behavior;




    private archimate_Behavior archimate_behavior;




    private List<archimate_Behavior> archimate_behaviors;


    public archimate_Behavior(
    ) {
        this.archimate_behaviors = new ArrayList<>();
        this.archimate_passives = new ArrayList<>();
        this.archimate_behaviors = new ArrayList<>();
    }

    public archimate_Behavior(
        ArrayList<archimate_Behavior> archimate_behaviors,        ArrayList<archimate_Passive> archimate_passives,        ArrayList<archimate_Behavior> archimate_behaviors    ) {
        this.archimate_behaviors = archimate_behaviors;
        this.archimate_passives = archimate_passives;
        this.archimate_behaviors = archimate_behaviors;
    }


    public List<archimate_Behavior> getArchimate_behaviors() {
        return archimate_behaviors;
    }

    public void addArchimate_behavior(Archimate_behavior archimate_behavior) {
        this.archimate_behaviors.add(archimate_behavior);
    }
    public List<archimate_Passive> getArchimate_passives() {
        return archimate_passives;
    }

    public void addArchimate_passive(Archimate_passive archimate_passive) {
        this.archimate_passives.add(archimate_passive);
    }
    public archimate_Passive getArchimate_passive() {
        return archimate_passive;
    }

    public void setArchimate_passive(archimate_Passive archimate_passive) {
        this.archimate_passive = archimate_passive;
    }
    public archimate_Behavior getArchimate_behavior() {
        return archimate_behavior;
    }

    public void setArchimate_behavior(archimate_Behavior archimate_behavior) {
        this.archimate_behavior = archimate_behavior;
    }
    public archimate_Behavior getArchimate_behavior() {
        return archimate_behavior;
    }

    public void setArchimate_behavior(archimate_Behavior archimate_behavior) {
        this.archimate_behavior = archimate_behavior;
    }
    public List<archimate_Behavior> getArchimate_behaviors() {
        return archimate_behaviors;
    }

    public void addArchimate_behavior(Archimate_behavior archimate_behavior) {
        this.archimate_behaviors.add(archimate_behavior);
    }

}