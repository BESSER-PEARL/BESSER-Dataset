





import java.util.List;
import java.util.ArrayList;

public class ir_Schedule  {

    private String PriorityGraph;





    private ir_Actor ir_actor;




    private List<ir_Action> ir_actions;


    public ir_Schedule(
        String PriorityGraph    ) {
        this.PriorityGraph = PriorityGraph;
        this.ir_actions = new ArrayList<>();
    }

    public ir_Schedule(
        String PriorityGraph        ArrayList<ir_Action> ir_actions    ) {
        this.PriorityGraph = PriorityGraph;
        this.ir_actions = ir_actions;
    }

    public String getPrioritygraph() {
        return PriorityGraph;
    }

    public void setPrioritygraph(String PriorityGraph) {
        this.PriorityGraph = PriorityGraph;
    }

    public ir_Actor getIr_actor() {
        return ir_actor;
    }

    public void setIr_actor(ir_Actor ir_actor) {
        this.ir_actor = ir_actor;
    }
    public List<ir_Action> getIr_actions() {
        return ir_actions;
    }

    public void addIr_action(Ir_action ir_action) {
        this.ir_actions.add(ir_action);
    }

}