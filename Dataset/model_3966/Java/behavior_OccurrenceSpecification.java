





import java.util.List;
import java.util.ArrayList;

public class behavior_OccurrenceSpecification extends InteractionFragment {






    private behavior_GeneralOrdering behavior_generalordering;




    private List<behavior_GeneralOrdering> behavior_generalorderings;




    private behavior_ExecutionSpecification behavior_executionspecification;




    private behavior_GeneralOrdering behavior_generalordering;




    private behavior_ExecutionSpecification behavior_executionspecification;




    private List<behavior_GeneralOrdering> behavior_generalorderings;


    public behavior_OccurrenceSpecification(
    ) {
        super(
        );
        this.behavior_generalorderings = new ArrayList<>();
        this.behavior_generalorderings = new ArrayList<>();
    }

    public behavior_OccurrenceSpecification(
        ArrayList<behavior_GeneralOrdering> behavior_generalorderings,        ArrayList<behavior_GeneralOrdering> behavior_generalorderings    ) {
        this.behavior_generalorderings = behavior_generalorderings;
        this.behavior_generalorderings = behavior_generalorderings;
    }


    public behavior_GeneralOrdering getBehavior_generalordering() {
        return behavior_generalordering;
    }

    public void setBehavior_generalordering(behavior_GeneralOrdering behavior_generalordering) {
        this.behavior_generalordering = behavior_generalordering;
    }
    public List<behavior_GeneralOrdering> getBehavior_generalorderings() {
        return behavior_generalorderings;
    }

    public void addBehavior_generalordering(Behavior_generalordering behavior_generalordering) {
        this.behavior_generalorderings.add(behavior_generalordering);
    }
    public behavior_ExecutionSpecification getBehavior_executionspecification() {
        return behavior_executionspecification;
    }

    public void setBehavior_executionspecification(behavior_ExecutionSpecification behavior_executionspecification) {
        this.behavior_executionspecification = behavior_executionspecification;
    }
    public behavior_GeneralOrdering getBehavior_generalordering() {
        return behavior_generalordering;
    }

    public void setBehavior_generalordering(behavior_GeneralOrdering behavior_generalordering) {
        this.behavior_generalordering = behavior_generalordering;
    }
    public behavior_ExecutionSpecification getBehavior_executionspecification() {
        return behavior_executionspecification;
    }

    public void setBehavior_executionspecification(behavior_ExecutionSpecification behavior_executionspecification) {
        this.behavior_executionspecification = behavior_executionspecification;
    }
    public List<behavior_GeneralOrdering> getBehavior_generalorderings() {
        return behavior_generalorderings;
    }

    public void addBehavior_generalordering(Behavior_generalordering behavior_generalordering) {
        this.behavior_generalorderings.add(behavior_generalordering);
    }

}