





import java.util.List;
import java.util.ArrayList;

public class nosql_KeySpace  {

    private String replicationFactor;
    private String replicaPlacementStrategy;
    private String name;



    public nosql_KeySpace(
        String replicationFactor,        String replicaPlacementStrategy,        String name    ) {
        this.replicationFactor = replicationFactor;
        this.replicaPlacementStrategy = replicaPlacementStrategy;
        this.name = name;
    }


    public String getReplicationfactor() {
        return replicationFactor;
    }

    public void setReplicationfactor(String replicationFactor) {
        this.replicationFactor = replicationFactor;
    }
    public String getReplicaplacementstrategy() {
        return replicaPlacementStrategy;
    }

    public void setReplicaplacementstrategy(String replicaPlacementStrategy) {
        this.replicaPlacementStrategy = replicaPlacementStrategy;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}