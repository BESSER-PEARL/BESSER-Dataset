





import java.util.List;
import java.util.ArrayList;

public class nosql_KeySpace  {

    private String replicaPlacementStrategy;
    private String name;
    private String replicationFactor;



    public nosql_KeySpace(
        String replicaPlacementStrategy,        String name,        String replicationFactor    ) {
        this.replicaPlacementStrategy = replicaPlacementStrategy;
        this.name = name;
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
    public String getReplicationfactor() {
        return replicationFactor;
    }

    public void setReplicationfactor(String replicationFactor) {
        this.replicationFactor = replicationFactor;
    }


}