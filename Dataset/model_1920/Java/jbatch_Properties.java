





import java.util.List;
import java.util.ArrayList;

public class jbatch_Properties  {

    private String partition;





    private jbatch_CheckpointAlgorithm jbatch_checkpointalgorithm;




    private jbatch_Analyzer jbatch_analyzer;




    private jbatch_Listener jbatch_listener;




    private List<jbatch_Property> jbatch_propertys;




    private jbatch_PartitionReducer jbatch_partitionreducer;




    private jbatch_PartitionPlan jbatch_partitionplan;




    private jbatch_PartitionMapper jbatch_partitionmapper;




    private jbatch_Step jbatch_step;


    public jbatch_Properties(
        String partition    ) {
        this.partition = partition;
        this.jbatch_propertys = new ArrayList<>();
    }

    public jbatch_Properties(
        String partition        ArrayList<jbatch_Property> jbatch_propertys    ) {
        this.partition = partition;
        this.jbatch_propertys = jbatch_propertys;
    }

    public String getPartition() {
        return partition;
    }

    public void setPartition(String partition) {
        this.partition = partition;
    }

    public jbatch_CheckpointAlgorithm getJbatch_checkpointalgorithm() {
        return jbatch_checkpointalgorithm;
    }

    public void setJbatch_checkpointalgorithm(jbatch_CheckpointAlgorithm jbatch_checkpointalgorithm) {
        this.jbatch_checkpointalgorithm = jbatch_checkpointalgorithm;
    }
    public jbatch_Analyzer getJbatch_analyzer() {
        return jbatch_analyzer;
    }

    public void setJbatch_analyzer(jbatch_Analyzer jbatch_analyzer) {
        this.jbatch_analyzer = jbatch_analyzer;
    }
    public jbatch_Listener getJbatch_listener() {
        return jbatch_listener;
    }

    public void setJbatch_listener(jbatch_Listener jbatch_listener) {
        this.jbatch_listener = jbatch_listener;
    }
    public List<jbatch_Property> getJbatch_propertys() {
        return jbatch_propertys;
    }

    public void addJbatch_property(Jbatch_property jbatch_property) {
        this.jbatch_propertys.add(jbatch_property);
    }
    public jbatch_PartitionReducer getJbatch_partitionreducer() {
        return jbatch_partitionreducer;
    }

    public void setJbatch_partitionreducer(jbatch_PartitionReducer jbatch_partitionreducer) {
        this.jbatch_partitionreducer = jbatch_partitionreducer;
    }
    public jbatch_PartitionPlan getJbatch_partitionplan() {
        return jbatch_partitionplan;
    }

    public void setJbatch_partitionplan(jbatch_PartitionPlan jbatch_partitionplan) {
        this.jbatch_partitionplan = jbatch_partitionplan;
    }
    public jbatch_PartitionMapper getJbatch_partitionmapper() {
        return jbatch_partitionmapper;
    }

    public void setJbatch_partitionmapper(jbatch_PartitionMapper jbatch_partitionmapper) {
        this.jbatch_partitionmapper = jbatch_partitionmapper;
    }
    public jbatch_Step getJbatch_step() {
        return jbatch_step;
    }

    public void setJbatch_step(jbatch_Step jbatch_step) {
        this.jbatch_step = jbatch_step;
    }

}