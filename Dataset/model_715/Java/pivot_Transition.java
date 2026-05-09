





import java.util.List;
import java.util.ArrayList;

public class pivot_Transition extends Namespace {

    private String kind;





    private pivot_Constraint pivot_constraint;




    private pivot_Trigger pivot_trigger;




    private pivot_Behavior pivot_behavior;




    private pivot_Vertex pivot_vertex;




    private pivot_Vertex pivot_vertex;




    private pivot_Region pivot_region;




    private pivot_Constraint pivot_constraint;




    private pivot_Vertex pivot_vertex;




    private pivot_Behavior pivot_behavior;




    private pivot_Vertex pivot_vertex;




    private pivot_Region pivot_region;




    private List<pivot_Trigger> pivot_triggers;


    public pivot_Transition(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.pivot_triggers = new ArrayList<>();
    }

    public pivot_Transition(
        String kind        ArrayList<pivot_Trigger> pivot_triggers    ) {
        this.kind = kind;
        this.pivot_triggers = pivot_triggers;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_Trigger getPivot_trigger() {
        return pivot_trigger;
    }

    public void setPivot_trigger(pivot_Trigger pivot_trigger) {
        this.pivot_trigger = pivot_trigger;
    }
    public pivot_Behavior getPivot_behavior() {
        return pivot_behavior;
    }

    public void setPivot_behavior(pivot_Behavior pivot_behavior) {
        this.pivot_behavior = pivot_behavior;
    }
    public pivot_Vertex getPivot_vertex() {
        return pivot_vertex;
    }

    public void setPivot_vertex(pivot_Vertex pivot_vertex) {
        this.pivot_vertex = pivot_vertex;
    }
    public pivot_Vertex getPivot_vertex() {
        return pivot_vertex;
    }

    public void setPivot_vertex(pivot_Vertex pivot_vertex) {
        this.pivot_vertex = pivot_vertex;
    }
    public pivot_Region getPivot_region() {
        return pivot_region;
    }

    public void setPivot_region(pivot_Region pivot_region) {
        this.pivot_region = pivot_region;
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public pivot_Vertex getPivot_vertex() {
        return pivot_vertex;
    }

    public void setPivot_vertex(pivot_Vertex pivot_vertex) {
        this.pivot_vertex = pivot_vertex;
    }
    public pivot_Behavior getPivot_behavior() {
        return pivot_behavior;
    }

    public void setPivot_behavior(pivot_Behavior pivot_behavior) {
        this.pivot_behavior = pivot_behavior;
    }
    public pivot_Vertex getPivot_vertex() {
        return pivot_vertex;
    }

    public void setPivot_vertex(pivot_Vertex pivot_vertex) {
        this.pivot_vertex = pivot_vertex;
    }
    public pivot_Region getPivot_region() {
        return pivot_region;
    }

    public void setPivot_region(pivot_Region pivot_region) {
        this.pivot_region = pivot_region;
    }
    public List<pivot_Trigger> getPivot_triggers() {
        return pivot_triggers;
    }

    public void addPivot_trigger(Pivot_trigger pivot_trigger) {
        this.pivot_triggers.add(pivot_trigger);
    }

}