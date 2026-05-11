





import java.util.List;
import java.util.ArrayList;

public class ir_State  {

    private String PriorityGraph;
    private String Action2TargetMap;
    private String name;





    private ir_Schedule ir_schedule;




    private ir_Schedule ir_schedule;


    public ir_State(
        String PriorityGraph,        String Action2TargetMap,        String name    ) {
        this.PriorityGraph = PriorityGraph;
        this.Action2TargetMap = Action2TargetMap;
        this.name = name;
    }


    public String getPrioritygraph() {
        return PriorityGraph;
    }

    public void setPrioritygraph(String PriorityGraph) {
        this.PriorityGraph = PriorityGraph;
    }
    public String getAction2targetmap() {
        return Action2TargetMap;
    }

    public void setAction2targetmap(String Action2TargetMap) {
        this.Action2TargetMap = Action2TargetMap;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ir_Schedule getIr_schedule() {
        return ir_schedule;
    }

    public void setIr_schedule(ir_Schedule ir_schedule) {
        this.ir_schedule = ir_schedule;
    }
    public ir_Schedule getIr_schedule() {
        return ir_schedule;
    }

    public void setIr_schedule(ir_Schedule ir_schedule) {
        this.ir_schedule = ir_schedule;
    }

}