





import java.util.List;
import java.util.ArrayList;

public class graphbt_Node  {

    private String id;
    private int index;





    private graphbt_BehaviorTree graphbt_behaviortree;


    public graphbt_Node(
        String id,        int index    ) {
        this.id = id;
        this.index = index;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public graphbt_BehaviorTree getGraphbt_behaviortree() {
        return graphbt_behaviortree;
    }

    public void setGraphbt_behaviortree(graphbt_BehaviorTree graphbt_behaviortree) {
        this.graphbt_behaviortree = graphbt_behaviortree;
    }

}